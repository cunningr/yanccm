# YANCCM

YANCCM (pronounced yanc'em) - Yet Another Network Configuration and Change Management tool uses the nclient to implement configuration management procedures for network devices supporting the next generation network management protocol - NETCONF.

## Motivation

In modern network operations it is desirable to have a Source of Truth (SoT) as part of Network Configuration and Change Management (NCCM) automation.  This could be a CMDB or some other asset management system.  An Opensource example of this is [Netbox](https://netbox.readthedocs.io/en/stable/). The goal is to use the SoT to describe the complete network configuration and enable automated tooling to manage network device configuration compliance and change centrally as oppose to using the network itself as the "Source of Truth".

Although there are already many solutions for configuration management of network devices, they most commonly rely on interacting with a CLI and resulting unstructured data.  Tools such as Ansible, NAPALM, netmiko and nonir (to name a few) aim to solve some of the challenges of automating against traditional CLI by adding layers of abstraction and textFSM parsing to make different device versions and vendors 'look' as similar as possible.  Netconf as described in [RFC 6241](https://tools.ietf.org/html/rfc6241) is a next-generation management protocol intended to solve many of the issues plagued by such tools mentioned above.

In summary, some of the key operational functions required for advanced configuration management are now be implemented 'on-box' using the standards based NETCONF protocol, such as;

 * Configuration to ```candidate``` datastore
    * Validates configuration syntax without making changes operational
    * Enables accurate calculation of **resulting 'diffs'**
 * **Commit** and **commit-confirmed**
    * In combination with the candidate datastore enables the possibility to 'dry-run' changes
    * Enables **automatic configuration rollback** in the event any change is deemed failed
 * Configuration **merge** and **replace** operations
    * Enables the administrator to easily restore configurations from an offline configuration store (E.g. rollback, backup/restore)

However, until more recently (we are now in 2021) the capabilities and coverage of Netconf across the major vendors has been patchy and somewhat incomplete.

Some of the basic goals include:

 * Commit/Diff configurations across multiple devices in a single transaction reverting configuration automatically on error
 * Restore device configurations to a 'known good' configuration version
 * Describe a Job in a simple format containing a list of devices and configurations:
    * Retrieve device attributes and/or credentials from an external SoT source (E.g. Netbox or some other)
    * Device config operation merge|replace|delete|diff
    * Job commit type (E.g. with rollback/commit confirm)
    * Ability to retrieve (results, logs etc.) and replay.

## Components

 * YANCCM - This code project provides the logical glue.
 * MongoDB - Provides a ConfigDB for storing device configuration and change history in order to facilitate compliance checks, rollback, backup and restore of device configuration.
 * Netbox - Provides Source of Truth (SoT) for network configuration data.

## Project Status - PoC

The current project status provides 'Proof of Concept' and although the integration components can easily be deployed using Docker tools there is some effort required for the initial setup. 

## Features

| ID | Short Name | Description | Status |
|:---:|:---:|:---|:---:|
| F001 | Job Spec | Allow users to specify configurations for multiple devices in a single YAML file for the following operations: config-diff, commit-confirm, commit | COMPLETE |
| F002 | CLI | Provide basic CLI tools for submitting jobs | COMPLETE |
| F003 | SoT Integration | Use a rest API to retrieve inventory data from a CMDB/SoT tool such as Netbox | COMPLETE |
| F004 | Configuration Compliance | Store device configurations in a document DB and provide CLI to compare saved config against actual device configuration for compliance.  Device scope can be selected based on --site or --device using query API on SoT  | COMPLETE |
| F005 | Restore configuration | Use the configuration DB to restore known good configuration | COMPLETE |
| F006 | Compliance from Template | Use custom fields in SoT to associate Day0 config templates, render template base on SoT queried data and check for compliance against live devices and print diffs | COMPLETE |
| F007 | Deploy Template | Use custom fields in SoT to associate Day0 config templates, render template base on SoT queried data and deploy configuration to live devices | COMPLETE |
| F008 | Configuration History | Track 10 previous device configurations in ConfigDB with associated meta data (E.g. JobID).  ConfigDB should be updated after a successful commit | NEW |
| F008 | Auto Compliance | Before making any device config changes, check for compliance against last known config.  Include an option to disable auto-compliance --no-check | NEW |
| F008 | Job History | Establish a history of Job | NEW |
