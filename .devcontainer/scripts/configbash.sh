
# Save bash history each time a command is used ... /root/commandhistory is mounted to a volume so it
# survives between container restarts
echo "export PROMPT_COMMAND='history -a'" >> "/root/.bashrc"
echo "export HISTFILE=/root/commandhistory/.bash_history" >> "/root/.bashrc"
mkdir -p /root/commandhistory
touch /root/commandhistory/.bash_history

# Git command prompt
git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1 
echo "if [ -f \"$HOME/.bash-git-prompt/gitprompt.sh\" ]; then GIT_PROMPT_ONLY_IN_REPO=1 && GIT_PROMPT_FETCH_REMOTE_STATUS=0 && source $HOME/.bash-git-prompt/gitprompt.sh; fi" >> "/root/.bashrc"
