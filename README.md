# Welcome to EOSFactory v2.1

[EOSFactory](http://eosfactory.io/) is a Python-based [EOS](https://eos.io) smart-contract development & testing framework, created by [Tokenika](https://tokenika.io).

The goal is to achieve a similar functionality to Ethereum's [Truffle Framework](http://truffleframework.com/).

With a single command-line interface you can create a private testnet and then compile, unit-test and deploy EOS smart-contracts.

All of this using simple yet powerful [Python3](https://www.python.org/) syntax.

## Why it’s needed?

Undoubtedly, everything that *EOSFactory* offers can be done with the official EOSIO toolset, i.e. `cleos` and `eosiocpp`. Does it make *EOSFactory* just a simple alternative to those tools? Not really.

Try to go through [EOS tutorials](https://github.com/EOSIO/eos/wiki/Tutorial-eosio-token-Contract) based on `cleos` and you'll see how much concentration is required to follow those simple examples without making a single mistake. And now imagine doing it 10 or 100 times. Surely, it's a daunting task!

Code development and unit-testing involve tasks that need to be executed hundreds of times, and each time in exactly the same way and exactly the same context. Therefore those tasks need to be fully automated, as otherwise a lot of time is being wasted and, what’s even worse, a lot of additional uncertainty is introduced. Manually performed actions are prone to errors.

And this is what *EOSFactory* actually brings to the table: an easy & intuitive way to automate the process of dealing with smart-contracts. Write down, in the form of a Python script, what needs to be done multiple times in exactly the same way and exactly the same context, and then just run the script. *EOSFactory* will take care of everything else: it will compile your smart-contract, create a new testnet, deploy the contract, invoke its methods and verify the response, then tear down the testnet, and finally report the results. And all of this done in a couple of seconds.

## Main features

#### 1. Object-oriented

When you use tools like `cleos` all you have at your disposal is issuing separate, one-off commands, as `cleos` is not able to keep your state. Thus each time you interact with a contract, you need to tell `cleos` which contract and which account you mean. Contrary to that, in *EOSFactory* everything is an object. You create a contract (or an account), keep reference to it and then invoke its various methods.

#### 2. Simple syntax

The front-end of *EOSFactory* is simply a Python3 *Command Line Interface*. This way you can interact with EOS smart-contract, and prove it works as expected, without having to deal with the complexity of a low-level language like C++. In most cases Python’s syntax is clear for everyone.

#### 3. Real testnet

As EOS full node is very quick we don’t need to rely on a testnet simulator similar to [TestRPC](https://github.com/trufflesuite/ganache-cli) in Ethereum. Instead, we can work with a real testnet and this makes unit-tests much more reliable. Thus *EOSFactory* has the ability to launch and tear down an EOS testnet in a very efficient way, so that you can fully test your smart-contract in a couple of seconds and do it multiple times.

#### 4. Support for both local and remote testnet

Performing unit tests on a public testnet is much more complex than using a local one where you have full control. The whole infrastructure of *EOSFactory* is designed in such a way that the same unit test is able to work in both environments, and switching between them is just a matter of changing one parameter.

#### 5. Aliases for account names

*EOSIO* accounts are indexed by their names, thus those names have to be unique within the blockchain namespace and have to follow specific restrictions. As a result, most of the human readable combinations are already taken, even in a testnet environment. *EOSFactory* hides the actual names of an *EOSIO* accounts behind a system of human-friendly aliases.

#### 6. Truly cross-platform

We make sure everything we do is fully compatible with Windows - our toolset enables you to run an EOS node and interact with it on any operating system, including Windows, MacOS and Linux.

## Architecture

*EOSFactory* is composed of two layers:
- C++ client (i.e. `cleos`) connected to an EOS node (i.e. `nodeos`) running a private or public testnet,
- Python wrapper acting as a convenient human-oriented interface.

Using Python will allow us to build [interactive tutorials](http://eosfactory.io/build/html/) for EOS smart-contracts.

## User documentation

* [Introduction to EOSFactory](http://eosfactory.io/build/html/tutorials/00.IntroductionToEOSFactory.html)
* [Installing EOSFactory](http://eosfactory.io/build/html/tutorials/01.InstallingEOSFactory.html)
* [Interacting with EOS Contracts in EOSFactory](http://eosfactory.io/build/html/tutorials/02.InteractingWithEOSContractsInEOSFactory.html)
* [Building and deploying EOS Contracts in EOSFactory](http://eosfactory.io/build/html/tutorials/03.BuildingAndDeployingEOSContractsInEOSFactory.html)
* [Working with EOS Contracts using EOSFactory in VSC](http://eosfactory.io/build/html/tutorials/04.WorkingWithEOSContractsUsingEOSFactoryInVSC.html)
* [Interacting with Public Testnet](http://eosfactory.io/build/html/tutorials/05.InteractingWithPublicTestnet.html)

## Use cases

* [Wallet Class](http://eosfactory.io/build/html/cases/02_wallet/case.html)
* [Symbolic Names](http://eosfactory.io/build/html/cases/03_symbolic_names/case.html)
* [Account Class](http://eosfactory.io/build/html/cases/04_account/case.html)
* [Master Account](http://eosfactory.io/build/html/cases/05_master_account/case.html)

## Developer documentation

Please refer to [this index of Python modules](http://eosfactory.io/build/html/py-modindex.html) which constitute the front-end of *EOSFactory*.

## Release notes

Please refer to [this document](http://eosfactory.io/build/html/releases/ReleaseNotesVersion2.1.html).

## Roadmap

Our long-term goal is to turn *EOSFactory* into a comprehensive IDE (Integrated Development Environment) for EOS smart-contracts, smilar to Ethereum's [Truffle Framework](https://truffleframework.com/).

- [Plan for Subsequent EOSFactory Releases](http://eosfactory.io/build/html/roadmap/PlanForSubsequentEOSFactoryReleases.html)
- [Long-term EOSFactory Roadmap](http://eosfactory.io/build/html/roadmap/LongTermEOSFactoryRoadmap.html)

## Support

For issues not covered in the documentation there is a dedicated [EOS Factory Support](https://t.me/EOSFactorySupport) channel on Telegram.

## Licence

This code is provided as is, under [MIT Licence](LICENCE).
