Role Name [![Build Status](https://travis-ci.com/kornsn/ansible_db.svg?branch=master)](https://travis-ci.com/kornsn/ansible_db)
=========

Ansible db role for otus hw ansible-4

Requirements
------------

...

Role Variables
--------------

- mongo_port: 27017
- mongo_bind_ip: 127.0.0.1
- env: local

Dependencies
------------

...

Example Playbook
----------------

    - hosts: servers
      become: true
      vars:
        mongo_bind_ip: 0.0.0.0
      roles:
         - ansible_db

License
-------

BSD

Author Information
------------------

Sergey Korneev
