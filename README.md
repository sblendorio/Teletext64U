# Teletext 64 Ultimate

Teletext program showing live pages from the internet for the Commodore 64 Ultimate and other Ultimate products that have networking capabilities

Currently only supporting NOS Teletekst (Dutch Teletext). Other Teletext services will be added later.

## Description
It is 100% teletext compliant by using proper teletext character sets including the special graphic (mosaic) characters and support for the most common diacrits / accent marks. It runs in hires bitmap mode to support all the required foreground/background color combinations. To make the look & feel even more authentic, it uses a super bright RGB palette; so no washed out default C64 colors.

It uses the same internet feed as the Dutch mobile apps. To make it feel even more like on TV, the header row is injected with the current date with a page number top left. Entering page numbers works like as on a remote. Just type 3 digits and the requested page will be fetched, if available. Browse through sub pages with the cursor up/down keys and the Home key brings you to page 101 with the latest news. It also supports fast text you see at the bottom row. These are mapped to the C64U’s functions keys.

Although the C64U has excellent networking capabilities, it unfortunately is restricted to HTTP. That does not bring us very far with basically every site running secure HTTPS these days. So I wrote a little Python program for PC/Mac/Linux/.. that handles the secure HTTPS connections. 

## Feature list
- Full support for NOS Teletekst (Dutch teletext)
- Auto 60 second refresh - always have the latest news on you screen, handy if you have your C64U hooked up to a separate screen; refresh time can be adjusted to your liking
- Fast text support via function keys (resembling the red, green, yellow and cyan quick access keys from the TV-remote)
- Two custom hand crafted 6x6 pixel character sets (thin & bold) - this leaves toom for 1 pixel row of background color at the top and bottom of each character. This leads to a much better overall looking teletext screen imo.
- Switch between the thin and bold fonts on the fly within the program


## Tools used for this project
CC65
VSCode
CharPad

## Source code
Will be added later.

## Credits and Licensing

### Third-Party Libraries
This project incorporates the following third-party library:

* **[ultimateii-dos-lib](https://github.com/xlar54/ultimateii-dos-lib)** by xlar54
    * **License:** [GNU General Public License v3.0](https://github.com/xlar54/ultimateii-dos-lib/blob/master/LICENSE)
    * **Usage:** Used for Ultimate II+ DOS and Network integration.

### License
This entire project is licensed under the **GNU General Public License v3.0**. 

As required by the GPL-3.0, the source code for this project is freely available. You may find the full text of the license in the `LICENSE` file in the root directory. The original license for `ultimateii-dos-lib` can be found in the `/lib/ultimateii-dos-lib/` folder.