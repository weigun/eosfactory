
import json

import eosfactory.core.logger as logger
import eosfactory.core.errors as errors
import eosfactory.core.interface as interface
import eosfactory.core.eosjs.base as base_commands


class GetInfo(base_commands.Command):
    """Get current blockchain information.

    - **parameters**::

        is_verbose: If `0`, do not print unless on error; if `-1`, 
            do not print. Default is `1`.

    - **attributes**::

        json: The json representation of the object.
        is_verbose: If set, print output.
    """
    def __init__(self, is_verbose=1):
        base_commands.Command.__init__(self, base_commands.config_rpc(), 
            """
    ;(async () => {
        result = await rpc.get_info()
        console.log(JSON.stringify(result))    
    })()
            """, is_verbose)

        self.head_block = self.json["head_block_num"]
        self.head_block_time = self.json["head_block_time"]
        self.last_irreversible_block_num \
            = self.json["last_irreversible_block_num"]

        self.printself()

    def __str__(self):
        return json.dumps(self.json, sort_keys=True, indent=4)


class GetActions(base_commands.Command):
    """Retrieve all actions with specific account name referenced in authorization or receiver.

    Note that available actions are filtered. By default, all actions are
    filered off. To see the actions, the node has to be restarted with the --filter-on option.

    Args:
        account (str): Name of account to query on.
        pos (int): Sequence number of action for this account, -1 for last. 
            Default is -1.
        offset (int): Get actions [pos,pos+offset] for positive offset or 
            [pos-offset,pos) for negative offset. Default is 1.
        json (bool): Responce received as JSON, if any. Default is ``False``.
        full (bool): Don't truncate action json. Default is ``False``.
        pretty (bool): Pretty print full action json. Default is ``False``.
        console (bool): print console output generated by action. Default 
            is ``False``.
        is_verbose (bool): If *False* do not print. Default is ``True``.
    """
    def __init__(
        self, account, pos=-1, offset=1, 
        json=True, full=False, pretty=False, console=False, is_verbose=True):

        args = [interface.account_arg(account), str(pos), str(offset)]
        
        if json:
            args.append("--json")
        if full:
            args.append("--full")
        if pretty:
            args.append("--pretty")
        if console:
            args.append("--console")
        # base_commands.Command.__init__(self, args, "get", "actions", is_verbose)

        self.printself()


class GetBlock(base_commands.Command):
    """Retrieve a full block from the blockchain.

    Args:
        block_number (int): The number of the block to retrieve.
        lock_id (str): The ID of the block to retrieve, if set, defaults to "".   
        is_verbose (bool): If ``False``, print a message. Default is ``True``.
        
    Attributes:
        json (json): The json representation of the block.
        block_num (int): The block number.
        timestamp (str): The block timestamp.
    """
    def __init__(self, block_number, block_id=None, is_verbose=1):
        if block_id:
            base_commands.Command.__init__(self, base_commands.config_rpc(),
                """
        (async (block_num_or_id) => {
            result = await rpc.get_block(block_num_or_id)
            console.log(JSON.stringify(result))

        })("%s")
                """ % (block_id), is_verbose)
        else:
            base_commands.Command.__init__(self, base_commands.config_rpc(),
                """
        (async (block_num_or_id) => {
            result = await rpc.get_block(block_num_or_id)
            console.log(JSON.stringify(result))

        })(%d)
                """ % (block_number), is_verbose)                        

        self.block_num = self.json["block_num"]
        self.timestamp = self.json["timestamp"]

        self.printself()


class GetAccounts(base_commands.Command):
    """Retrieve accounts associated with a public key.

    Args:
        key (str or .interface.Key): The public key to retrieve accounts for.
        is_verbose (bool): If *False* do not print. Default is *True*.

    Attributes:
        names (list): The retrieved list of accounts.
    """
    def __init__(self, key, is_verbose=True):
        
        try:
            base_commands.Command.__init__(self, base_commands.config_rpc(),
                """
            (async (public_key) => {
                result = await rpc.history_get_key_accounts(public_key)
                console.log(JSON.stringify(result))

            })("%s")    
                """ % (interface.key_arg(key, is_owner_key=True, is_private_key=False)),
                is_verbose=is_verbose)
        except Exception as e:
            raise errors.Error(
                "Is History API Plugin enabled on the blockchain node?\n\n" \
                                                                    + str(e))

        self.names = self.json['account_names']
        self.printself()


class GetCode(base_commands.Command):
    """Retrieve the code and ABI for an account.

    Args:
        account (str or .interface.Account): The account to retrieve.
        code (str): If set, the name of the file to save the contract 
            .wast/wasm to.
        abi (str): If set, the name of the file to save the contract .abi to.
        wasm (bool): Save contract as wasm.
        is_verbose (bool): If *False* do not print. Default is *True*.

    Attributes:
        code_hash (str): The hash of the code.
    """
    def __init__(
            self, account, code="", abi="", 
            wasm=False, is_verbose=True):

        account_name = interface.account_arg(account)

        args = [account_name]
        if code:
            args.extend(["--code", code])
        if abi:
            args.extend(["--abi", abi])
        if wasm:
            args.extend(["--wasm"])

        # base_commands.Command.__init__(self, args, "get", "code", is_verbose)

        msg = str(self.out_msg)
        self.json["code_hash"] = msg[msg.find(":") + 2 : len(msg) - 1]
        self.code_hash = self.json["code_hash"]
        self.printself()


class GetTable(base_commands.Command):
    """Retrieve the contents of a database table

    Args:
        table (str): The name of the table as specified by the contract abi.        
        scope (str or .interface.Account): The scope within the account in 
            which the table is found.
        binary (bool): Return the value as BINARY rather than using abi to 
            interpret as JSON. Default is *False*.
        limit (int): The maximum number of rows to return. Default is 10.
        lower (str): JSON representation of lower bound value of key, 
            defaults to first.
        upper (str): JSON representation of upper bound value value of key, 
            defaults to last.
        index (int or str): Index number, 1 - primary (first), 2 - secondary 
            index (in order defined by multi_index), 3 - third index, etc.
            Number or name of index can be specified, 
            e.g. 'secondary' or '2'.
        key_type (str): The key type of --index, primary only supports 
            (i64), all others support (i64, i128, i256, float64, float128, 
            ripemd160, sha256).
            Special type 'name' indicates an account name.
        enncode_type (str): The encoding type of key_type 
            (i64 , i128 , float64, float128) only support decimal 
            encoding e.g. 'dec'i256 - supports both 'dec' and 'hex', 
            ripemd160 and sha256 is 'hex' only.
        reverse (bool): Iterate in reverse order.
        is_verbose (bool): If *False* do not print. Default is *True*.
    """
    def __init__(
            self, account, table, scope,
            binary=False, 
            limit=10, lower="", upper="", index="",
            key_type="", encode_type="", reverse=False, show_payer=False,
            is_verbose=True
            ):
        args = [interface.account_arg(account)]

        if not scope:
            scope=account
        else:
            try:
                scope_name = scope.name
            except:
                scope_name = scope

        args.append(scope_name)
        args.append(table)

        if binary:
            args.append("--binary")
        if limit:
            args.extend(["--limit", str(limit)])
        if lower:
            args.extend(["--lower", lower])
        if upper:
            args.extend(["--upper", upper])
        if index:
            args.extend(["--index", str(index)])
        if key_type:
            args.extend(["--key-type", key_type])
        if encode_type:
            args.extend(["--encode-type", encode_type])
        if reverse:
            args.append("--reverse")
        if show_payer:
            args.append("--show-payer")

        # base_commands.Command.__init__(self, args, "get", "table", is_verbose)

        self.printself()
