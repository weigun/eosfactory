#include <cstdarg>

#include <boost/property_tree/json_parser.hpp>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string/replace.hpp>

#include <teos/item.hpp>
#include <teoslib/config.h>


std::string formatUsage(std::string unixUsage) {
#ifdef WIN32
  std::string windowsCmndUsage = unixUsage;
  boost::replace_all(windowsCmndUsage, "\"", "\"\"\"");
  boost::replace_all(windowsCmndUsage, "'", "\"");
  return windowsCmndUsage;
#else
  return unixUsage;
#endif
}

namespace teos
  {
    using namespace std;
    using namespace boost::property_tree;

    void output(const char* label, const char* format, ...) {
      printf("## %20s: ", label);

      string f(format);
      f += "\n";

      va_list argptr;
      va_start(argptr, format);
      vprintf(f.c_str(), argptr);
      va_end(argptr);
    }

    void output(const char* text, ...) {
      printf("## %s\n", text);
    }

    /***************************************************************************
    Definitions for the class Item.
    ****************************************************************************/

    ptree Item::getConfig(bool verbose) {
      ptree config;
      try
      {
        read_json(CONFIG_JSON, config);
      }
      catch (...) {
        boost::filesystem::path full_path(boost::filesystem::current_path());
        if (verbose) {
          printf("ERROR: Cannot read config file %s!\n", CONFIG_JSON);
          printf("Current path is: %s\n", full_path.string().c_str());
          printf("The config json file is expected there!");
        }
      }
      return config;
    }

    bool Item::verbose = false;

    /******************************************************************************
    Definitions for class 'ItemOptions'. Virtual definitions have to remain in 
    the header. Also the 'go' method, depending on virtual definitions has to be
    there.
    ******************************************************************************/

    template<class T>
    T ItemOptions<T>::getCommand() {
      return T();
    };

  }
