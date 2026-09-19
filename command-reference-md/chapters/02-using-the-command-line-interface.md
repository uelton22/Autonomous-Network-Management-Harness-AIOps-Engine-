# Capítulo 2: Using the Command-Line Interface

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Command Syntax

The command-line interface (CLI) is a text-based way to manage and monitor the system. You can access the CLI by using a direct serial connection or by using a remote logical connection with SSH. This chapter describes the CLI syntax, conventions, and modes. It contains the following sections: • Supported Platforms • Command Syntax • Common Parameter Values • Using the "No" Form of a Command • CLI Output Filtering • Command Modes • Command Completion and Abbreviation • CLI Error Messages • CLI Line-Editing Conventions • Using CLI Help • Accessing the CLI SUPPORTED PLATFORMS Consult Hardware and Software Compatibility in Release Notes to check supported platforms. COMMAND SYNTAX A command is one or more words that might be followed by one or more parameters. Parameters can be required or optional values. Some commands, such as show ip route or clear mac address-table, do not require parameters. Other commands, such as aaa authentication, require that you supply a value after the command. You must type the parameter values in a specific order, and optional parameters follow required parameters. The following example describes the aaa authentication command syntax: aaa authentication user username password password [group admin | config |

## Using the "No" Form of a Command

audit] • aaa authentication is the command name. • user and password are parameters and represent required options that user must enter after the command keyword. • username and password are required parameters that user must enter after the user and password keywords, respectively. • [group {admin | config | audit}] is an optional parameter that could be (or could not be) inserted after the password password parameter. Only one of the available values (admin, config or audit) must be typed after the group keyword. The Command Reference lists each command by the command name and provides a brief description of the command. Each command reference also contains the following information: • Format: shows the command keywords and the required and optional parameters. • Mode: identifies the command mode you must be in to access the command. • Default: shows the default value, if any, of a configurable setting on the device. The show commands also contain a description of the information that the command shows. COMMON PARAMETER VALUES Parameter values might be names (strings) or numbers. Spaces could be used as part of a name parameter only for line<N> parameters, without any kind of delimiter. For example, the expression System Name with Spaces will be recognized as a unique value when used as a parameter for the command snmp-server contact. Empty strings are not valid user-defined strings. USING THE "NO" FORM OF A COMMAND The no keyword is a specific form of an existing command and does not represent a new or distinct command. Almost every configuration command has a no form. In general, use the no form to reverse the action of a command or reset a value back to the default. For example, the no shutdown configuration command reverses the shutdown of an interface. Use the command without the keyword no to re-enable a disabled feature

## CLI Output Filtering

or to enable a feature that is disabled by default. Only the configuration commands are available in the no form. CLI OUTPUT FILTERING Many CLI show commands include considerable content to display to the user. This can make output confusing and cumbersome to parse through to find the information of desired importance. The CLI Output Filtering feature allows the user, not only when executing CLI show display commands, but specially on these cases, to optionally specify arguments to filter the CLI output to display only desired information. The result is to simplify the display and make it easier for the user to find the information the user is interested in. The main functions of the CLI Output Filtering feature are: • Pagination Control • Supports enabling/disabling paginated output for all CLI commands. When disabled, output is displayed in its entirety. When enabled, output is displayed page-by-page such that content does not scroll off the terminal screen until the user presses a key to continue. -- more --, next page: Space, continue: g, quit: ˆC is displayed at the end of each page. • When pagination is enabled, press the return key to advance a single line, press q, Q or Ctrl+C to stop pagination, press g or G to continue up to the end of the output, or press any other key to advance a whole page. These keys are not configurable. • Output Filtering • "Grep"-like control for modifying the displayed output to only show the userdesired content. • Filter displayed output to only include lines containing a specified string match. • Filter displayed output to exclude lines containing a specified string match. • Filter displayed output to only include lines including and following a specified string match. • String matching should be case insensitive. • Pagination, when enabled, also applies to filtered output.

## Command Completion and Abbreviation

Example: The following shows an example of the extensions made to the CLI commands for the Output Filtering feature.

```text
DmOS# show running-config ?
```

Possible completions: aaa Configure authentication, authorization and accounting alias Create command alias. anti-ip-spoofing Anti ip-spoofing configuration clock Set the system clock dot1q VLAN Manager Protocol gpon GPON configuration | Output modifiers

```text
DmOS# show running-config | ?
```

Possible completions: append Append output text to a file begin Begin with the line that matches best-effort Display data even if data provider is unavailable or continue loading from file in presence of failures count Count the number of lines in the output csv Show table output in CSV format de-select De-select columns details Display default values COMMAND MODES The CLI groups the commands into modes, according to the command function. Each of the command modes supports specific software commands. The commands in a particular mode will not to be available until you switch to that given mode. You can execute Operational commands in the Configure commands mode by usign the do keyword. COMMAND COMPLETION AND ABBREVIATION Command completion finishes spelling the command when you type enough letters of a command to uniquely identify the command keyword. Once you have entered enough letters, press the TAB key to complete the word or press SPACE BAR and let that system resolves the command directly from the short version.

## CLI Error Messages

Command abbreviation allows you to execute a command when you have entered there are enough letters to uniquely identify the command. You must enter all of the required keywords and parameters before you enter the command.

```text
DmOS# re
```

Possible completions: reboot Reboot the system reboot-forced Reboot the system without any checks request Request system operations DmOS(config)# interface gigabit-ethernet 1/1/ Possible completions: 1 2 3 4 5 6 7 8 9 10 11 12 The TAB key will complete the command if there is only one candidate command. Otherwise, a list of all possible commands will be showed. CLI ERROR MESSAGES If you enter a command and the system is unable to execute it, an error message appears. Table 1: CLI Error Messages describes the most common CLI error messages. Table 1: CLI Error Messages Message Text Description syntax error: unknown Indicates that the command there is not in the CLI. command syntax error: unknown Indicates that the argument there is not for the command. argument syntax error: unknown Indicates that the value inserted there is not for the comelement mand.

## CLI Line-Editing Conventions

CLI LINE-EDITING CONVENTIONS Table 2: CLI Editing Conventions describes the key combinations you can use to edit commands or increase the speed of command entry. Table 2: CLI Editing Conventions Key Sequence Description Ctrl-H or Backspace Delete previous character. Ctrl-A Go to beginning of line. Ctrl-E Go to end of line. Ctrl-F Go forward one character. Ctrl-B Go backward one character. Ctrl-D Delete current character. Ctrl-U or Ctrl-X Delete to beginning of line. Ctrl-K Delete to end of line. Ctrl-W Delete previous word. Ctrl-P Go to previous line in history buffer. Ctrl-R Rewrites or pastes the line. Ctrl-N Go to next line in history buffer. Ctrl-Z Return to root command prompt.

## Using CLI Help

Table 2: CLI Editing Conventions Key Sequence Description <Tab> Command-line completion. Exit Go to next lower command prompt. ? List available commands, keywords, or parameters. USING CLI HELP Enter a question mark (?) at the command prompt to display the commands available in the current mode.

```text
DmOS# ?
```

Possible completions: autowizard Automatically query for mandatory elements clear Clear equipment settings and counters commit Confirm a pending commit compare Compare running configuration to another configuration or a file complete-on-space Enable/disable completion on space config Manipulate software configuration information copy Copy files to a remote server display-level Configure show command display level exit Exit the management session DM4610(config)# ? Possible completions: aaa Configure authentication, authorization and accounting alias Create command alias. anti-ip-spoofing anti ip-spoofing configuration clear Clear equipment settings and counters clock Set the system clock copy Copy a list entry dot1q VLAN Manager Protocol gpon GPON configuration hostname Hostname for this equipment Enter a question mark (?) after each word you enter to display available command keywords or parameters. DmOS(config)# router static ? Possible completions: <a.b.c.d/x> or <x:x:x:x::x/x> IP/IPv6 prefix <network>/<length> 0.0.0.0/0 DmOS(config)# interface gigabit-ethernet ? Possible completions: <id:string> 1/1/1 1/1/2 1/1/3 1/1/4 1/1/5 1/1/6 1/1/7 1/1/8 1/1/9 1/1/10 1/1/11 1/1/12 If there are no additional command keywords or parameters, or if additional parameters are optional, the following message appears in the output: <cr> You can also enter a question mark (?) after typing one or more characters of a word to list the available command or parameters that begin with the letters, as shown in the following example:

```text
DmOS# show i?
```

Possible completions: interface Status information about interfaces inventory Physical inventory information ip Display ip information ipv6 Display ipv6 information | Output modifiers <cr>

## Special Characters on CLI

ACCESSING THE CLI You can access the CLI by using a direct console connection or by using a SSH connection from a remote management host. To establish a terminal connection using console interface (VT100), a proper serial cable (provided with the equipment) must be connected between the equipment terminal port and the PC serial port. Take care to avoid potential difference between RJ45 pin 4 from Switch (signal ground) and DB9 pin 5 from the PC. If it occurs, it may cause damages to the PC and to the equipment’s serial interfaces. To access the terminal, select the serial port of your preference and set the following values on the VT100 emulator (factory default values of equipment): • Baud Rate: 9600bit/s • Data: 8 bits • Flow Control: none • Stop Bit: 1 bit • Parity: none Once the access was successful, a login screen must appear. The login factory defaults are: • User: admin • Password: For the initial connection, you could use also a SSH client, connecting an Ethernet port of your PC to the management port of the switch (10/100Base-T) and accessing the default IP address: 192.168.0.25 (with a 255.255.255.0 subnet mask and without a default gateway), with the same credentials of VT100 terminal. You can set the network configuration information manually, or you can configure the system to accept these settings from a DHCP server on your network. For more information, see Network Interface Commands. specialCharactersCli SPECIAL CHARACTERS ON CLI Some characters have special interpretations for the command line. Table 3: Special Characters on CLI Character Description ? List available commands, keywords, or parameters.

```text
! and # It is interpreted as a comment.
\ It is interpreted as escape character.
```

It is interpreted as output modifier. Used with output filter- | ing commands. ; Used to indicate end of a command line. “ Used to delimit a string. If it is necessary to use the characters above on a string, put the string between doublequotes (“).
