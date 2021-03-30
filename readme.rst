Kill proces

if debug is on, after closing Pycharm the process still may run.
port 5000 is taken then.
- $sudo lsof -i :5000
- $sudo kill -9 <pid>
