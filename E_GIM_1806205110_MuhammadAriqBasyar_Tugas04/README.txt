Wellcome To My Mini Project!

                        ↱~~~~~~~~~~~~~~~~~~~~~~~~~↰
                        | By Muhammad Ariq Basyar |
                        |       1806205110        |
                        |   All Rights Reserved   |
                        ↳~~~~~~~~~~~~~~~~~~~~~~~~~↵

Installation:
  Firstly, make sure even you have installed pygame, here is the installation
(depends on your operating system):

  Windows:
      pip install pygame

  Linux:
      sudo pip3 install pygame

  Mac OS:
  1.  Install Xcode: In Finder, open Applications, App Store. Search for Xcode and click Get to install the Xcode developer tools. 
      You’ll need these developer tools to run some of the command-line instructions in a Terminal window below.


  2.  Install XQuartz: Go to http://xquartz.macosforge.org and download the current version of XQuartz (2.7.7 as of this writing). 
      Open your Downloads folder, double-click on the XQuartz-2.7.7.dmg file, then double-click on the XQuartz.pkg package file 
      and follow the instructions to complete the installation.


  3.  Open a Terminal (command-line) window: Go to Applications, Utilities, and double-click Terminal. Your command-line Terminal
      window will open. All the following commands must be typed exactly as they appear in the Terminal window, one line at a time.


  4.  Install Homebrew: At the Terminal command line prompt, type the following as a single full line (you may want to expand your
      Terminal window wider to allow it to fit, but it’s okay if it wraps around):
      
      	ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
      
      then, hit return. Homebrew is a free program that helps you install Python, Pygame, and other programs on a Mac.


  5.  Prepare Homebrew for use: At the Terminal prompt, type each of the following three commands exactly as shown – the second two 
      may take a few moments to run and will show several screens of information, but keep following the steps one line at a time.
      
      	echo export PATH=’/usr/local/bin:$PATH’ >> ~/.bash_profile
      	brew update
      	brew doctor


  6.  Install Python 3 for Pygame: At the Terminal prompt, type:
      
      	brew install python3
      
      This will install a separate Python 3 specifically for Pygame use – this is required for all the following steps to work.


  7.  Install Mercurial: Still at the Terminal prompt, type:
      
	brew install mercurial
      
      Mercurial is a free source control management system that this installation of Pygame requires on a Mac.


  8.  Install Pygame dependencies: Pygame requires several other helper programs, called dependencies, so that it can show 
      animations, play sounds, and create game graphics. Type the following three lines at the Terminal command prompt, hitting return after each line
      
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
      	brew tap homebrew/headonly
      	brew install smpeg
      
      (NOTE 18JUL2015: Updated to reflect changes to the smpeg library; if you have any trouble here, try brew install –HEAD smpeg instead, with two 
      dashes/hyphens before the HEAD option).
      Each command will take a few moments to run and display screens full of information; keep going, you’re almost done…


  9.  Install Pygame: Type the following line at the Terminal prompt and hit return:
      
	sudo pip3 install hg+http://bitbucket.org/pygame/pygame
      
      You may have to enter an administrator password (your password, or ask an IT administrator for help at school, work, or the library), and the 
      installation may take a few minutes.




To Play:
    Double click the "E_GIM_1806205110_MuhammadAriqBasyar_Tugas04.pyw"
    You can :
	jump with Space or Arrow-up 
	pause the game with Esc
