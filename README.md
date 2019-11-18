# php

[![Build Status](https://drone.owncloud.com/api/badges/owncloud-ansible/php/status.svg)](https://drone.owncloud.com/owncloud-ansible/php)

> **WARNING**: This Ansible role is currently in beta state. Use it at your own risk.


Ansible role to setup PHP

## Table of content

* [Default Variables](#default-variables)
  * [php_allow_url_fopen](#php_allow_url_fopen)
  * [php_apc_enable_cli](#php_apc_enable_cli)
  * [php_apc_enabled](#php_apc_enabled)
  * [php_apc_shm_size](#php_apc_shm_size)
  * [php_date_timezone](#php_date_timezone)
  * [php_default_version](#php_default_version)
  * [php_disable_functions](#php_disable_functions)
  * [php_display_errors](#php_display_errors)
  * [php_display_startup_errors](#php_display_startup_errors)
  * [php_error_reporting](#php_error_reporting)
  * [php_expose_php](#php_expose_php)
  * [php_file_uploads](#php_file_uploads)
  * [php_fpm_enabled](#php_fpm_enabled)
  * [php_fpm_listen](#php_fpm_listen)
  * [php_fpm_listen_allowed_clients](#php_fpm_listen_allowed_clients)
  * [php_fpm_pm_max_children](#php_fpm_pm_max_children)
  * [php_fpm_pm_max_spare_servers](#php_fpm_pm_max_spare_servers)
  * [php_fpm_pm_min_spare_servers](#php_fpm_pm_min_spare_servers)
  * [php_fpm_pm_start_servers](#php_fpm_pm_start_servers)
  * [php_max_execution_time](#php_max_execution_time)
  * [php_max_file_uploads](#php_max_file_uploads)
  * [php_max_input_time](#php_max_input_time)
  * [php_max_input_vars](#php_max_input_vars)
  * [php_memory_limit](#php_memory_limit)
  * [php_opcache_blacklist_filename](#php_opcache_blacklist_filename)
  * [php_opcache_enable_cli](#php_opcache_enable_cli)
  * [php_opcache_enabled](#php_opcache_enabled)
  * [php_opcache_interned_strings_buffer](#php_opcache_interned_strings_buffer)
  * [php_opcache_max_accelerated_files](#php_opcache_max_accelerated_files)
  * [php_opcache_max_file_size](#php_opcache_max_file_size)
  * [php_opcache_max_wasted_percentage](#php_opcache_max_wasted_percentage)
  * [php_opcache_memory_consumption](#php_opcache_memory_consumption)
  * [php_opcache_revalidate_freq](#php_opcache_revalidate_freq)
  * [php_opcache_revalidate_path](#php_opcache_revalidate_path)
  * [php_opcache_validate_timestamps](#php_opcache_validate_timestamps)
  * [php_output_buffering](#php_output_buffering)
  * [php_packages_extra](#php_packages_extra)
  * [php_packages_state](#php_packages_state)
  * [php_post_max_size](#php_post_max_size)
  * [php_realpath_cache_size](#php_realpath_cache_size)
  * [php_sendmail_path](#php_sendmail_path)
  * [php_session_cookie_lifetime](#php_session_cookie_lifetime)
  * [php_session_gc_divisor](#php_session_gc_divisor)
  * [php_session_gc_maxlifetime](#php_session_gc_maxlifetime)
  * [php_session_gc_probability](#php_session_gc_probability)
  * [php_session_save_handler](#php_session_save_handler)
  * [php_session_save_path](#php_session_save_path)
  * [php_short_open_tag](#php_short_open_tag)
  * [php_upload_max_filesize](#php_upload_max_filesize)
  * [php_webserver_enabled](#php_webserver_enabled)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### php_allow_url_fopen

#### Default value

```YAML
php_allow_url_fopen: On
```

### php_apc_enable_cli

#### Default value

```YAML
php_apc_enable_cli: '1'
```

### php_apc_enabled

#### Default value

```YAML
php_apc_enabled: true
```

### php_apc_shm_size

#### Default value

```YAML
php_apc_shm_size: 96M
```

### php_date_timezone

#### Default value

```YAML
php_date_timezone: America/Chicago
```

### php_default_version

#### Default value

```YAML
php_default_version: '7.2'
```

### php_disable_functions

#### Default value

```YAML
php_disable_functions: []
```

### php_display_errors

#### Default value

```YAML
php_display_errors: Off
```

### php_display_startup_errors

#### Default value

```YAML
php_display_startup_errors: Off
```

### php_error_reporting

#### Default value

```YAML
php_error_reporting: E_ALL & ~E_DEPRECATED & ~E_STRICT
```

### php_expose_php

#### Default value

```YAML
php_expose_php: On
```

### php_file_uploads

#### Default value

```YAML
php_file_uploads: On
```

### php_fpm_enabled

#### Default value

```YAML
php_fpm_enabled: false
```

### php_fpm_listen

#### Default value

```YAML
php_fpm_listen: 127.0.0.1:9000
```

### php_fpm_listen_allowed_clients

#### Default value

```YAML
php_fpm_listen_allowed_clients: 127.0.0.1
```

### php_fpm_pm_max_children

#### Default value

```YAML
php_fpm_pm_max_children: 50
```

### php_fpm_pm_max_spare_servers

#### Default value

```YAML
php_fpm_pm_max_spare_servers: 5
```

### php_fpm_pm_min_spare_servers

#### Default value

```YAML
php_fpm_pm_min_spare_servers: 5
```

### php_fpm_pm_start_servers

#### Default value

```YAML
php_fpm_pm_start_servers: 5
```

### php_max_execution_time

#### Default value

```YAML
php_max_execution_time: '3600'
```

### php_max_file_uploads

#### Default value

```YAML
php_max_file_uploads: '20'
```

### php_max_input_time

#### Default value

```YAML
php_max_input_time: '{{ php_max_execution_time }}'
```

### php_max_input_vars

#### Default value

```YAML
php_max_input_vars: '1000'
```

### php_memory_limit

#### Default value

```YAML
php_memory_limit: 256M
```

### php_opcache_blacklist_filename

#### Default value

```YAML
php_opcache_blacklist_filename: ''
```

### php_opcache_enable_cli

#### Default value

```YAML
php_opcache_enable_cli: '1'
```

### php_opcache_enabled

#### Default value

```YAML
php_opcache_enabled: true
```

### php_opcache_interned_strings_buffer

#### Default value

```YAML
php_opcache_interned_strings_buffer: '16'
```

### php_opcache_max_accelerated_files

#### Default value

```YAML
php_opcache_max_accelerated_files: '4096'
```

### php_opcache_max_file_size

#### Default value

```YAML
php_opcache_max_file_size: '0'
```

### php_opcache_max_wasted_percentage

#### Default value

```YAML
php_opcache_max_wasted_percentage: '5'
```

### php_opcache_memory_consumption

#### Default value

```YAML
php_opcache_memory_consumption: '96'
```

### php_opcache_revalidate_freq

#### Default value

```YAML
php_opcache_revalidate_freq: '2'
```

### php_opcache_revalidate_path

#### Default value

```YAML
php_opcache_revalidate_path: '0'
```

### php_opcache_validate_timestamps

#### Default value

```YAML
php_opcache_validate_timestamps: '1'
```

### php_output_buffering

#### Default value

```YAML
php_output_buffering: '4096'
```

### php_packages_extra

Can be used to install other dependency packages e.g. gcc (required by pecl).

#### Default value

```YAML
php_packages_extra: []
```

### php_packages_state

Use `present` to make sure it's installed, or `latest` if you want to upgrade.

#### Default value

```YAML
php_packages_state: present
```

### php_post_max_size

#### Default value

```YAML
php_post_max_size: 32M
```

### php_realpath_cache_size

#### Default value

```YAML
php_realpath_cache_size: 32K
```

### php_sendmail_path

#### Default value

```YAML
php_sendmail_path: /usr/sbin/sendmail -t -i
```

### php_session_cookie_lifetime

#### Default value

```YAML
php_session_cookie_lifetime: 0
```

### php_session_gc_divisor

#### Default value

```YAML
php_session_gc_divisor: 1000
```

### php_session_gc_maxlifetime

#### Default value

```YAML
php_session_gc_maxlifetime: 1440
```

### php_session_gc_probability

#### Default value

```YAML
php_session_gc_probability: 1
```

### php_session_save_handler

#### Default value

```YAML
php_session_save_handler: files
```

### php_session_save_path

#### Default value

```YAML
php_session_save_path: ''
```

### php_short_open_tag

#### Default value

```YAML
php_short_open_tag: Off
```

### php_upload_max_filesize

#### Default value

```YAML
php_upload_max_filesize: 64M
```

### php_webserver_enabled

Set this to `False` if you're not using PHP with a webserver e.g. Apache/Nginx.

#### Default value

```YAML
php_webserver_enabled: true
```

## Dependencies

None.

## License

Apache-2.0

## Author

Robert Kaussow
