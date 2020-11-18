# Flash-Text-Editor

## Installation

#### For both windows and linux:

- ``python -m pip install requirements.txt``

- In the terminal/cmd, run ``setup.py`` like this: ``python setup.py``



## What is Flash Text Editor?
Is a text editor that is easy to use, with variety of options, it is called "Flash" because it is light text editor.

## Why did you choose to create a text editor ?
One day, i was searching for a project to create, i decided i want to build a gui application , then i thought it is better to create a text editor than any other project, since it has variety options which would teach me a lot about gui stuffs in programming
## Why did you choose Tkinter library, why not other libraries like PyQt?
Firstly, Tkinter is a very wide library with so many functionalities that are easy to use!,beside the fact that it has many resources on internet (google,stackoverflow,python forums,and documentations), Secondly,i did NOT prefer PyQT over Tkinter because PyQt is originally made is C++ and there are not many resources over the internet for PyQt like with Tkinter, so it take longer time to find things related to PyQt (in case official docs didnt help understanding something),Finally, i am going to say that tkinter UI is old, which make PyQt better here, but i still decided to go with Tkinter because i want to learn stuffs about gui, so i didnt care much about UI modernity.

## What is the structure of this project in general?
The structure of this project is based on classes , and there is composition relationship between classes on different level (has-a-relationship),each class is on a different file, for better readability.

## Exploring Flash
Lets start exploring the text editor:
- ### File:
- #### New file:

![New File](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/newfile.gif)

- #### Open File:

![Open File](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/openfile.gif)

- #### Save as:

![Save as](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/saveas.gif)


- #### Close File:

![Close File](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/closefile.gif)

- #### Exit:

![Exit](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/exit.gif)


Now for the second menu which is "Edit":


-Copy

-Paste

-Cut

-Select All

-Undo

-Redo

-Delete

each of them has their own key (for example copy->ctrl+c, which is well known)


Now for View menu:

- #### Font Size:

![Font Size](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/font%20size.gif)

- #### Font Family:

![Font Family](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/font%20family.gif)


*Note: The reason i chose "Font size" rather than "zooming in and out" is because tkinter doesnt have a real zooming option, so font size was the best option out there.


Search menu:

- #### Find... :

![Find](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/find.gif)


- #### Find and Replace:

![Find and Replace](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/find%20and%20replace.gif)


*On a side note, Find all might be slow if you are writing a very big program,because for now the functionality works on while loop.

Finally we have Theme menu:
- #### Text Color:

![Text Color](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/textcolor.gif)


- #### Cursor Color:

![Cursor Color](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/Cursor.gif)


- #### Selector Color:

![Selector Color](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/Selector.gif)


- #### themes:

![themes](https://github.com/ghazigamer/Flash-Text-Editor/blob/master/gifs/Themes.gif)



## Great, that was a small tour to the text editor, back to some disscussions:
### Mistakes i have learnt:

- Lack of Testing (which i learnt it the hard way, it is very important to milk whatever functionality you are testing)


### Things that improved me :

- Planning for the project (drawing diagrams and writing explanation for many stuffs)

- Not giving up ever!


## Is this project complete?

- For now this is basically complete, but i will add more things to this project in the future.


## Conclusion:
Any question, suggestion, and critism is welcome, if you found an issue, please do tell.




Thank you.
