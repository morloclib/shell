RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

def good(msg):
    return f"{GREEN}{msg}{RESET}"

def bad(msg):
    return f"{RED}{msg}{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"

def testEqual(msg, x, y, results):
    (nfails, ntests) = results
    if(x == y):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected: {y!r}")
        print(f"    got:      {x!r}")
        return (nfails + 1, ntests + 1)

def testTrue(msg, x, results):
    return testEqual(msg, x, True, results)

def testGe(msg, x, y, results):
    (nfails, ntests) = results
    if(x >= y):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected: >= {y!r}")
        print(f"    got:         {x!r}")
        return (nfails + 1, ntests + 1)

def testNonEmpty(msg, x, results):
    (nfails, ntests) = results
    if(len(x) > 0):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected non-empty, got: {x!r}")
        return (nfails + 1, ntests + 1)

def testContains(msg, xs, x, results):
    (nfails, ntests) = results
    if(x in xs):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected {x!r} in list")
        return (nfails + 1, ntests + 1)

def printMsg(msg, x):
    print(info(msg))
    return x

def printResult(x):
    if(x[0] == 0):
        print(good(f"All {x[1]!s} tests pass"))
    else:
        print(bad(f"{x[0]!s}/{x[1]!s} tests failed"))
    return x

def cleanDir(path):
    import shutil
    import os
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
    return None
