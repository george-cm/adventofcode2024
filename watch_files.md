echo "09" | xargs -t -I{} watchmedo shell-command -W --patterns='day{}.py;day{}_test.py' --recursive --command='pytest -v -s day{}/day{}_test.py' . 
