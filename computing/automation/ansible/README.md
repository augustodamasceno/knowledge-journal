##  Automation with Ansible.
> Copyright (c) 2023, Augusto Damasceno.  
> All rights reserved.   
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Ansible Directory Structure    
1. inventories  
> This folder contains inventory files that define the hosts and groups of hosts where Ansible will run.  
2. roles
> This directory holds Ansible roles, which are reusable units of automation.  
3. playbooks  
> This folder contains Ansible playbooks, which define what tasks to execute on which hosts.  
4. group_vars  
> This folder stores variables that apply to groups of hosts defined in inventories.  
5. host_vars  
> This folder stores host-specific variables.  
6. templates  
> This folder contains Jinja2 template files used to generate dynamic configuration files.  
7. files  
> This folder holds static files to be copied to remote servers.  
8.  ansible.cfg
> Configuration file for Ansible. 
9. requirements.yml
> Defines external Ansible roles or collections that need to be installed using ansible-galaxy  
10. hosts file  
> The hosts file (also called an inventory file) defines the managed nodes and groups. It contains information like IP addresses, hostnames, and groupings.  
Location
* Linux  
> /etc/ansible/hosts  
* FreeBSD
> /usr/local/etc/ansible/hosts  
* macOS  
  * Homebrew
    > /usr/local/etc/ansible/hosts
  * Pip
    > /etc/ansible/hosts
* Windows (No default location)
> ansible-playbook -i <CUSTOM_PATH> playbook.yml
* Specify on ansible.cfg  
```yml
[defaults]
inventory = /path/to/custom/hosts
```

# Copy file from control node to managed node  
* The file is associated with the user myuser
* The file is associated with the group mygroup
* The file mode bits is 0700
* Activate privilege escalation
```yaml
- name: Copy a file
  become: yes
  copy:
    src: /path/to/file/control_node/file
    dest: /path/to/file/managed_node/file
    mode: 0700
    owner: "myuser"
    group: "mygroup"
```

# Install Software with Package Managers
> All examples re-synchronize the package index before install  
## APT  
```yaml
- name: Install Vim
  become: yes
  apt:
    name: vim
    state: present
    update_cache: yes
```
## YUM  
```yaml
- name: Install Vim
  become: yes
  yum:
    name: vim-enhanced
    state: present
    update_cache: yes
```
## DNF   
```yaml
- name: Install Vim
  become: yes
  dnf:
    name: vim-enhanced
    state: present
    update_cache: yes
```
## Zypper
```yaml
- name: Install Vim
  become: yes
  zypper:
    name: vim
    state: present
    refresh: yes
```
## Pacman
```yaml
- name: Install Vim
  become: yes
  pacman:
    name: vim
    state: present
    update_cache: yes
```
## FreeBSD
```yaml
- name: Install Vim
  become: yes
  pkgng:
    name: vim
    state: present
    update_cache: yes
```

## References: 
* https://docs.ansible.com
* https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8&format=html