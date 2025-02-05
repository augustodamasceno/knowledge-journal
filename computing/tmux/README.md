# TMUX  
> Share shell session and avoid broken SSH connection problems  
## Run tmux
```bash
tmux
```
## Attach the session on another terminal/ssh connection
```bash
tmux -a
```
## List all tmux sessions
```bash
tmux -ls
```
## Attach a session on another terminal/ssh connection by ID or name
```bash
tmux attach-session -t <SESSION>
```
## Copy tmux buffer last 3000 lines and save to tmux-buffer.txt
> Prefix normally is Ctrl + b
```bash
# press prefix + :
capture-pane -S -3000
# press prefix + :
save-buffer tmux-buffer.txt
```