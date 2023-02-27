<a name="readme-top"></a>
<br />
<div align="center">

<h3 align="center">Example implementation of an Ansible network module and resource</h3>

  <p align="center">
    Implementation of a fake Ansible network module and connection resource, used to learn how
    it all ties together.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains a [custom module](library/unicolet_ping.py) and a [connection resource](library/plugins/httpapi/unicolet.py) for a fake
network device called unicolet.

As of now the module does not realy use the network resource (no actual network call is made), however it shouws how the
two interact. This is illustrated by the `get_device_info()` call in the module, which calls the corresponding function in the resource.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python 3
* Ansible 7.2.0

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Create a pipenv, then install the required packages with `pipenv install`. Once you have a working ansible installation you'll need to
install additional ansible modules:

```sh
ansible-galaxy collection install ansible.netcommon:4.1.0
```

### Running the module

Run ansible as follows:

```sh
ANSIBLE_CONFIG=./ansible.cfg ansible -i inventory unicolet -m unicolet_ping
```

if all goes well you should see an output like the following:

```
PLAY [Ansible Ad-Hoc] *****************************************************************

TASK [unicolet_ping] ******************************************************************
ok: [unicolet]

PLAY RECAP ****************************************************************************
unicolet                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Play around with the python code and see how it can break, for example if you rename the `get_device_info` function
in the network resource.

### Installation

It is not possible to install or use this module as it's not really meant to work. Maybe in the future there will
be a full collection that can be installed through `ansible-galaxy`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

File an issue and preferrably a pull request. I'm not actively looking for contributions at this time so
delays in answering are to be expected.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

[@unicolet](https://github.com/unicolet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
