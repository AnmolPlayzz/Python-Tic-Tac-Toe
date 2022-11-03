<p align="center">
<img src="https://cdn.discordapp.com/attachments/904245641495060560/1037669250707501136/ttt.png" align="center" width="125px">
</p>
<h1 align="center" style="font-weight: bolder;">Python-Tic-Tac-Toe</h2>
<p align="center">A tic tac toe game made in python with 0 third party packages.</p>

---

<h2>What is this?</h2>

A recreation of the popular game tic-tac-toe which can be played in the terminal. Made using zero dependencies.

<h2>Why?</h2>

It was a school project and we gotta flex on our friends 💀.

<h2>How does this work?</h2>

The basic concept is as follows:
- We use a string which is exactly 9 characters long to store the progress of the game.
- Let's say the user playing as X entered 5, we need to add X to the fifth position in the string.
- To achieve this we reduce this number by 1

    ```py
    n-1 #n -> number entered by the user```
- Now, we set the index value of n-1 in the string as X.
- This code displays the string in the grid format
    
    ```py
    print(" "+l[0]+" | "+l[1]+" | "+l[2]+"")
    print("-----------")
    print(" "+l[3]+" | "+l[4]+" | "+l[5]+"")
    print("-----------")
    print(" "+l[6]+" | "+l[7]+" | "+l[8]+"")
    ```

---

Made with python and ♥ by @AnmolPlayzz and @iamaryaman