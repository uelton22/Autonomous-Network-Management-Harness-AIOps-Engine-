# Capítulo 15: ASCII Character Set and Hexadecimal Values

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## test cable-diagnostics through xmodem

### ASCII Character Set and Hexadecimal Values

• ASCII Character Set and Hexadecimal Values, on page 1140

### ASCII Character Set and Hexadecimal Values

Some commands described in the Cisco IOS documentation set, such as the escape-character line configuration command, require that you enter the decimal representation of an ASCII character. Other commands occasionally make use of hexadecimal (hex) representations. The below table provides character code translations from the decimal numbers to their hexadecimal and ASCII equivalents. It also provides the keyword entry for each ASCII character. For example, the ASCII carriage return (CR) is decimal 13. Entering Ctrl-M at your terminal generates decimal 13, which is interpreted as a CR. Note This document is a reference for only the standard ASCII character set. Extended ASCII character sets are not generally recommended for use in Cisco IOS commands. Extended ASCII character set references are widely available on the internet.

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| Decimal | Hex |  |  |  |
| 0 | 00 |  |  |  |
| 1 | 01 | SOH | Startofheading | Ctrl-A |
| 2 | 02 | STX | Startoftext | Ctrl-B |
| 3 | 03 | ETX | Break/endoftext | Ctrl-C |
| 4 | 04 | EOT | Endoftransmission | Ctrl-D |
| 5 | 05 | ENQ | Enquiry | Ctrl-E |
| 6 | 06 | ACK | Positiveacknowledgment | Ctrl-F |
| 7 | 07 | BEL | Bell | Ctrl-G |
| 8 | 08 | BS | Backspace | Ctrl-H |
| 9 | 09 | HT | Horizontaltab | Ctrl-I |
| 10 | 0A | LF | Linefeed | Ctrl-J |
| 11 | 0B | VT | Verticaltab | Ctrl-K |
| 12 | 0C | FF | Formfeed | Ctrl-L |
| 13 | 0D | CR | Carriagereturn(intheCLI,equivalenttotheEnteror Returnkey) | Ctrl-M |
| 14 | 0E | SO | Shiftout | Ctrl-N |

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| 15 | 0F | SI | Shiftin/XON(resumeoutput) | Ctrl-O |
| 16 | 10 | DLE | Datalinkescape | Ctrl-P |
| 17 | 11 | DC1 | Devicecontrolcharacter1 | Ctrl-Q |
| 18 | 12 | DC2 | Devicecontrolcharacter2 | Ctrl-R |
| 19 | 13 | DC3 | Devicecontrolcharacter3 | Ctrl-S |
| 20 | 14 | DC4 | Devicecontrolcharacter4 | Ctrl-T |
| 21 | 15 | NAK | Negativeacknowledgment | Ctrl-U |
| 22 | 16 | SYN | Synchronousidle | Ctrl-V |
| 23 | 17 | ETB | Endoftransmissionblock | Ctrl-W |
| 24 | 18 | CAN | Cancel | Ctrl-X |
| 25 | 19 | EM | Endofmedium | Ctrl-Y |
| 26 | 1A | SUB | Substitute/endoffile | Ctrl-Z |
| 27 | 1B | ESC | Escape | Ctrl-[ |
| 28 | 1C | FS | Fileseparator | Ctrl-\ |
| 29 | 1D | GS | Groupseparator | Ctrl-] |
| 30 | 1E | RS | Recordseparator | Ctrl-^ |
| 31 | 1F | US | Unitseparator | Ctrl-_ |
| 32 | 20 | SP | Space | Space |
| 33 | 21 | ! | ! | ! |
| 34 | 22 | " | " | " |
| 35 | 23 | # | # | # |
| 36 | 24 | $ | $ | $ |
| 37 | 25 | % | % | % |
| 38 | 26 | & | & | & |
| 39 | 27 | ’ | ’ | ’ |
| 40 | 28 | ( | ( | ( |
| 41 | 29 | ) | ) | ) |
| 42 | 2A | * | * | * |

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| 43 | 2B | + | + | + |
| 44 | 2C | , | , | , |
| 45 | 2D | - | - | - |
| 46 | 2E | . | . | . |
| 47 | 2F | / | / | / |
| 48 | 30 | 0 | Zero | 0 |
| 49 | 31 | 1 | One | 1 |
| 50 | 32 | 2 | Two | 2 |
| 51 | 33 | 3 | Three | 3 |
| 52 | 34 | 4 | Four | 4 |
| 53 | 35 | 5 | Five | 5 |
| 54 | 36 | 6 | Six | 6 |
| 55 | 37 | 7 | Seven | 7 |
| 56 | 38 | 8 | Eight | 8 |
| 57 | 39 | 9 | Nine | 9 |
| 58 | 3A | : | : | : |
| 59 | 3B | ; | ; | ; |
| 60 | 3C | < | < | < |
| 61 | 3D | = | = | = |
| 62 | 3E | > | > | > |
| 63 | 3F | ? | ? | ? |
| 64 | 40 | @ | @ | @ |
| 65 | 41 | A | A | A |
| 66 | 42 | B | B | B |
| 67 | 43 | C | C | C |
| 68 | 44 | D | D | D |
| 69 | 45 | E | E | E |
| 70 | 46 | F | F | F |

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| 71 | 47 | G | G | G |
| 72 | 48 | H | H | H |
| 73 | 49 | I | I | I |
| 74 | 4A | J | J | J |
| 75 | 4B | K | K | K |
| 76 | 4C | L | L | L |
| 77 | 4D | M | M | M |
| 78 | 4E | N | N | N |
| 79 | 4F | O | O | O |
| 80 | 50 | P | P | P |
| 81 | 51 | Q | Q | Q |
| 82 | 52 | R | R | R |
| 83 | 53 | S | S | S |
| 84 | 54 | T | T | T |
| 85 | 55 | U | U | U |
| 86 | 56 | V | V | V |
| 87 | 57 | W | W | W |
| 88 | 58 | X | X | X |
| 89 | 59 | Y | Y | Y |
| 90 | 5A | Z | Z | Z |
| 91 | 5B | [ | [ | [ |
| 92 | 5C | \ | \ | \ |
| 93 | 5D | ] | ] | ] |
| 94 | 5E | ^ | ^ | ^ |
| 95 | 5F | _ | _ | _ |
| 96 | 60 | ` | ` | ` |
| 97 | 61 | a | a | a |
| 98 | 62 | b | b | b |

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| 99 | 63 | c | c | c |
| 100 | 64 | d | d | d |
| 101 | 65 | e | e | e |
| 102 | 66 | f | f | f |
| 103 | 67 | g | g | g |
| 104 | 68 | h | h | h |
| 105 | 69 | i | i | i |
| 106 | 6A | j | j | j |
| 107 | 6B | k | k | k |
| 108 | 6C | l | l | l |
| 109 | 6D | m | m | m |
| 110 | 6E | n | n | n |
| 111 | 6F | o | o | o |
| 112 | 70 | p | p | p |
| 113 | 71 | q | q | q |
| 114 | 72 | r | r | r |
| 115 | 73 | s | s | s |
| 116 | 74 | t | t | t |
| 117 | 75 | u | u | u |
| 118 | 76 | v | v | v |
| 119 | 77 | w | w | w |
| 120 | 78 | x | x | x |
| 121 | 79 | y | y | y |
| 122 | 7A | z | z | z |
| 123 | 7B | { | { | { |
| 124 | 7C | \| | \| | \| |
| 125 | 7D | } | } | } |
| 126 | 7E | ~ | Tilde | ~ |

| NumericValues | ASCIICharacter | Meaning | KeyboardEntry |  |
| --- | --- | --- | --- | --- |
| 127 | 7F | DEL | Delete | Del |
