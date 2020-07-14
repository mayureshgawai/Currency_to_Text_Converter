<!-- 
git init
-> command for initializing repository on local git server

git add
-> this command used for add specific files on git

git push
-> pushing the files from local server to centralized git server

git commit
-> to add commit to save the particular changes in file

git status 
-> to check the file status whether thy are staged, edited, delted etc. -->

<!-- 
# Hello World 
## Desktop Application
_Italic_
**Strong Bold**
~~10000~~

[Visit Website](www.google.com "Google")

Images
![ui.jpg](ui.jpg)


Use `for` loop

```
def console_output():
    print("Hello")

```
 -->


# Hello World 
## Desktop Application

_Description_
    This application is the example of the User Interface developed using Python Interface Framework known as PyQt5.
It is just a simple text printing application consist of single _LineEdit_ and three different buttons for three different kinds of output.
    **Popup**
    Popup button generates a popup for a string entered in LineEdit.
    **Label**
    Label button assigns a label with the string in LineEdit.
    **Console**
    Nothing but simply prints LineEdit input in Console.

The input in LineEdit can be anything as it doesn't have any restrictions.

Images
![ui.jpg](ui.jpg)

#How it Works:

1. Enter any string Input in LineEdit
2. Press the button from your choice.


##Code for creating LineEdit and pushButtons in PyQt5

**pushButton**
```
self.pushButton.clicked.connect(self.hello_popup)
self.pushButton_2.clicked.connect(self.hello_console)
self.pushButton_3.clicked.connect(self.hello_label)
```

**LineEdit**
```
self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
self.lineEdit.setGeometry(QtCore.QRect(170, 30, 251, 20))
self.lineEdit.setObjectName("lineEdit")
```


#References:

**Package Installation**
    From python's official documentations online

[Visit](https://pypi.org/project/PyQt5/ "pypi.org")

**Step by Step Working**
    From YouTube Channels, Links mentioned below.

    1. [Tech with Tim](https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj "Visit Channel")

    2. [Programing Knowledge](https://www.youtube.com/watch?v=_bi0SqW_4L0&list=PLS1QulWo1RIZTkXbVkjr5Z3m-uMs05u7V "Visit ")