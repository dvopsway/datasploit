import importlib
import os
import sys
from glob import glob


def run(component, module_dir, m_input):
    dir_path = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), module_dir)
    sys.path.insert(0, dir_path)
    domain_files = glob("%s/%s_*.py" % (dir_path, component))
    active_modules = []
    for index, i in enumerate(domain_files):
        module_name = os.path.basename(os.path.splitext(i)[0])
        x = importlib.import_module(module_name)
        if not x.ENABLED:
            print "[-] Skipping %s because it is marked as disabled." % module_name.split("_")[1].title()
        else:
            active_modules.append(x)

    for x in active_modules:
        if "banner" in dir(x):
            x.banner()
        data = x.main(m_input)
        x.output(data, m_input)
