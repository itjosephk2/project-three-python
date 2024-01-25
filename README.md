# Dragon Ball Z Text Based Combat Game

![Macro Calculator mockup image](assets/readme-files/goku.png)

This a text based combat game almost like pookemon where you fight different Dragon Ball Z fighters against eachother. There is a main story mode which involves four chapters. You Travel through the desert searching for an item for master roshi as Goku. Fighting whoever comes in your path. Once you return eternal doom faces the very Island you love and know as Roshi's home. Do you have what it takes to save your friends Island. The is also a tutorial mode where you fight a weakened frieza as Goku in order to get used to the controls and flow of the game. There is also a free fight mode where you can choose your character and fight against any random fighter the computer chooses. 

Visit the deployed application [here]().

## Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    4. [Data Model](#data-model)
    5. [Flowchart](#flowchart)
2. [Features](#features)
    1. [Welcome Screen](#welcome-screen)
    2. [Main menu](#main-menu-screen)
    3. [Tutorial Screen](#tutorial-screen)
    4. [Story Screen](#story-screen)
    5. [Character Selection](#character-selection-screen)
    6. [HP Screen](#hp-screen)
    7. [Move Choice Screen](#move-choice-screen)
    8. [Enemy Turn](#enemy-turn-screen)
    9. [Enemy Move](#enemy-move-screen)
3. [Technologies Used](#technologies-used)
    1. [Language Used](#language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

* Provide a text based battle game that has a story mode, free battle mode and tutorial

* The story mode has multiple fights and text to create a sense of adventure with win and lose conditions.

* Provides input validation to help the user input the correct data.

* The program should keep running until the user decides otherwise.

### User Stories

* As a user, I want to receive information about the main objective of the program.

* As a user, I want to easily understand what input is needed on each step.

* As a user, I want to receive clear feedback in case I provide the wrong input.

* As a user, I want to be able to review the data I provided and correct it if needed.

* As a user, I want to know the remaining hp of the fighters to know where i stand in the battle after every attack

### Data Model

The main data for this game is the fighters. Theyre data is stored as objects where stats such as hp, attack, defence, special, speed.

There is input data collected and stored in variables for mening both for the main menu and the battle scene when a move is being selected

Damage calculation method takes in the appropriate damage of the move and a small and simple algorithym calculates the damage dealth based on the stats of the attacler and defender. This is then utilised to update the defending fighters remaining hp.

The remainning hp is utilised to display to the user how much health they have left. The hp stat is the overall hp the character starts with, which can be used to reset their hp to full if needed. 

### Flowchart

The following flowchart was designed using [Miro](https://miro.com/) in order to plan the logic to be implemented in the program.

![Game overview Flowchart](assets/readme-files/flow-chart.png)

As shown in the flowchart, this is the overall flow of the main menuing of the game

[Back to top ⇧](#Dragon-Ball-Z-Text-Based-Combat-Game)

## Features

### Welcome Screen

Introduce player to the game

![Welcome Screen](assets/readme-files/welcome-screen.png)

Due to the biological characteristics needed for the BMR calculation, sex has been used over gender.

### Main Menu Screen

Allow the users to select the game mode they wish to play

![Main Menu](assets/readme-files/main-menu.png)

### Tutorial Screen

Introduces the user to the tutorial fight and the objective of the battle.

![Tutorial Screen](assets/readme-files/tutorial-screen.png)

### Story Screen

One of numerous screens that display the content of the story. This lays out the main storyline and the context for the upcoming fight.
 
![Story Screen](assets/readme-files/story-screen.png)

### Character Selection Screen

Shows the menu for the character selection screen that is used for the free fight section of the main menu. The computer randomly chooses one of these characters for you to fight.

![Character Selection Screen](assets/readme-files/character-choice-screen.png)

### HP Screen

Allow the users to review the data input and give them the possibility to enter the data again if a mistake has been made.

![Review Data](assets/readme-files/review-data.png)
![Review Data Question](assets/readme-files/review-data-question.png)

### Move Choice Screen

The program use the [Mifflin-St Jeor formula](https://pubmed.ncbi.nlm.nih.gov/2305711/) to calculate the user's basal metabolic rate (BMR) using the input provided.

![BMR](assets/readme-files/bmr.png)

**Mifflin-St Jeor Formula**

*Male BMR* = [9.99 x weight (kg)] + [6.25 x height (cm)] – [4.92 x age (years)] + 5

*Female BMR* = [9.99 x weight (kg)] + [6.25 x height (cm)] – [4.92 x age (years)] – 161

### Enemy Turn Screen

The program use the the value of the selected activity level multiplied by the BMR to calculate the user's total daily energy expenditure (TDEE)..

![TDEE](assets/readme-files/tdee.png)

Activity Level | Value
---|---
No activity: | 1.2
A little activity: | 1.375
Some activity: | 1.55
A lot of activity: | 1.725
A TON of activity: | 1.9

### Enemy Move Screen

Calculate the total daily calories to be consumed by using the value of the selected goal multiplied by the TDEE.

![Calories Goal](assets/readme-files/calories-goal.png)

**Lose Weight**

Rate | Value
--- | ---
Slow | 0.91
Moderate | 0.82
Fast | 0.65

**Maintain Weight**

Keeps the same TDEE value.

**Gain Weight**

Rate | Value
--- | ---
Slow | 1.08
Moderate | 1.17
Fast | 1.34

[Back to top ⇧](#Dragon-Ball-Z-Text-Based-Combat-Game)

## Technologies Used

### Language Used

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

* [Pycharm](https://www.jetbrains.com/pycharm/) was used for writing code.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
 
* [Miro](https://miro.com/) was used to create the program flowchart.

[Back to top ⇧](#macro-calculator)

## Testing

### Testing User Stories

* As a user, I want to receive information about the main objective of the program.

    - Information about the program is presented in the welcome message explaining the use of the application.

    - Details are provided together with the results to further explain the different terms.

* As a user, I want to easily understand what input is needed on each step.

    - Input messages are being provided with detailed information on what the input needs to be.

    - Input messages text is colored in light green to make them noticeable.

* As a user, I want to receive clear feedback in case I provide the wrong input.

    - Error messages are provided explaining what is wrong with the input provided in case the wrong input is entered.

    - Some values as age, weight and height are being limited in order to gather the correct information and avoid mistypes.

    - Error messages have a red background to make them noticeable.

* As a user, I want to be able to review the data I provided and correct it if needed.

    - Added a feature where the user can easily see the data entered and decide to continue or enter the data again.

    - The data is being presented in table format to make it easier to review.

    - The input data is colored in light yellow to make it as clear as possible.

* As a user, I want the calculations to be displayed in a clear way and to be easy to understand.

    - Calculations are being formatted and presented at the end of the program with explanation for the different results.

    - The result data is colored in light yellow to make it as clear as possible.

### Code Validation

The [PEP8 online check](http://pep8online.com/) was used continuosly during the development proces to validate the Python code for PEP8 requirements. For this reason no before and after snapshots are available.

![PEP8 Code Validation](assets/readme-files/pep8-code-validation.png)

### Manual Testing

<table>
    <tr>
        <th>Feature</th>
        <th>Outcome</th>
        <th>Example</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Name Input</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/name-empty.png alt="Name value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Age Input</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/age-empty.png alt="Age value is empty"></td>
        <td>Pass</td>
    </tr>
        <td>Validate if value is too low</td>
        <td><img src=assets/readme-files/age-low.png alt="Age value is too low"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is too high</td>
        <td><img src=assets/readme-files/age-high.png alt="Age value is too high"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not an integer</td>
        <td><img src=assets/readme-files/age-not-int.png alt="Age value is not an integer"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Sex Selection</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/sex-empty.png alt="Sex value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if invalid value</td>
        <td><img src=assets/readme-files/sex-invalid.png alt="Sex value is invalid"></td>
        <td>Pass</td>
    </tr>
        <tr>
        <td rowspan=2>Unit Selection</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/unit-empty.png alt="Unit value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if invalid value</td>
        <td><img src=assets/readme-files/unit-invalid.png alt="Unit value is invalid"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=8>Weight Input</td>
        <td rowspan=2>Validate if value is empty</td>
        <td><img src=assets/readme-files/weight-kg-empty.png alt="Weight in kg value is empty"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/weight-lb-empty.png alt="Weight in lb value is empty"></td>
    </tr>
    </tr>
        <td rowspan=2>Validate if value is too low</td>
        <td><img src=assets/readme-files/weight-kg-low.png alt="Weight in kg value is too low"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/weight-lb-low.png alt="Weight in lb value is too low"></td>
    </tr>
    </tr>
        <td rowspan=2>Validate if value is too high</td>
        <td><img src=assets/readme-files/weight-kg-high.png alt="Weight in kg value is too high"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/weight-lb-high.png alt="Weight in lb value is too high"></td>
    </tr>
    <tr>
        <td rowspan=2>Validate if value is not an integer</td>
        <td><img src=assets/readme-files/weight-kg-not-int.png alt="Weight in kg value not an integer"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/weight-lb-not-int.png alt="Weight in lb value not an integer"></td>
    </tr>
    <tr>
        <td rowspan=8>Height Input</td>
        <td rowspan=2>Validate if value is empty</td>
        <td><img src=assets/readme-files/height-cm-empty.png alt="Height in cm value is empty"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/height-inch-empty.png alt="Height in inch value is empty"></td>
    </tr>
    </tr>
        <td rowspan=2>Validate if value is too low</td>
        <td><img src=assets/readme-files/height-cm-low.png alt="Height in cm value is too low"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/height-inch-low.png alt="Height in inch value is too low"></td>
    </tr>
    </tr>
        <td rowspan=2>Validate if value is too high</td>
        <td><img src=assets/readme-files/height-cm-high.png alt="Height in cm value is too high"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/height-inch-high.png alt="Height in inch value is too high"></td>
    </tr>
    <tr>
        <td rowspan=2>Validate if value is not an integer</td>
        <td><img src=assets/readme-files/height-cm-not-int.png alt="Height in cm value not an integer"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/height-inch-not-int.png alt="height in inch value not an integer"></td>
    </tr>
    <tr>
        <td rowspan=2>Activity Level Selection</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/activity-level-empty.png alt="Activity level value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if invalid value</td>
        <td><img src=assets/readme-files/activity-level-invalid.png alt="Activity level value is invalid"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Goal Selection</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/goal-empty.png alt="Goal value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if invalid value</td>
        <td><img src=assets/readme-files/goal-invalid.png alt="Goal value is invalid"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Rate Selection</td>
        <td rowspan=2>Validate if value is empty</td>
        <td><img src=assets/readme-files/lose-weight-rate-empty.png alt="Lose weight rate value is empty"></td>
        <td rowspan=2>Pass</td>
    </tr>
        <td><img src=assets/readme-files/gain-weight-rate-empty.png alt="Gain weight rate value is empty"></td>
    </tr>
    <tr>
        <td rowspan=2>Validate if invalid value</td>
        <td><img src=assets/readme-files/lose-weight-rate-invalid.png alt="Lose weight rate value is invalid"></td>
        <td rowspan=2>Pass</td>
    </tr>
    </tr>
        <td><img src=assets/readme-files/gain-weight-rate-invalid.png alt="Gain weight rate value is invalid"></td>
    <tr>
    <tr>
        <td rowspan=2>Diet Selection</td>
        <td>Validate if value is empty</td>
        <td><img src=assets/readme-files/diet-empty.png alt="Diet value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if invalid value</td>
        <td><img src=assets/readme-files/diet-invalid.png alt="Diet value is invalid"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Review Data</td>
        <td>Allow user to enter the data again</td>
        <td><img src=assets/readme-files/review-data-question.png alt="Review data question"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Restart Program</td>
        <td rowspan=2>Keep running or exit the program</td>
        <td><img src=assets/readme-files/restart-program.png alt="Exit the program"></td>
        <td rowspan=2>Pass</td>
    </tr>
    <tr>
        <td><img src=assets/readme-files/keep-running.png alt="Restart the program"></td></tr>
</table>

[Back to top ⇧](#macro-calculator)

## Deployment

The application has been deployed using [Heroku](https://id.heroku.com/) by following these steps:

[Heroku](https://id.heroku.com/) was used to deploy the application.

1. Create the requirements.txt file and run: `pip3 freeze > requirements.txt` in the console.
2. Commit changes and push them to GitHub.
3. Go to the Heroku's website.
4. From the Heroku dashboard, click on "Create new app".
5. Enter the "App name" and "Choose a region" before clicking on "Create app".
6. Go to "Config Vars" under the "Settings" tab.
7. Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
8. Add the Config Var, KEY: PORT and VALUE: 8000.
9. Go to "Buildpacks" section and click "Add buildpack".
10. Select "python" and click "Save changes"
11. Add "nodejs" buildpack as well using the same process.
12. Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
13. Go to "Connect to GitHub" section and "Search" the repository to be deployed.
14. Click "Connect" next the repository name.
15. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

[Back to top ⇧](#macro-calculator)

## Credits

### Content

* Inspiration for this game primarily comes from my childhood/aldut adddiction with the main line [pokemon](https://www.pokemon.com/us) games. The turn based battle game with the stats is almost entirely inspired by the [first gen pokemon games](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red,_Blue,_and_Yellow) and the idea for using dragon ball z charatcers comes both from my love for the [anime](https://en.wikipedia.org/wiki/Dragon_Ball_Z) and a [pokemon mod](https://www.pokeharbor.com/2021/05/dragon-ball-z-team-training/) which allowed you to use dragon ball z fighters instead of pokemon.

### Media
* The ascii art was primarily gotten from [Dragonball Ascii art](https://ascii.co.uk/art/dragonball).

### Code
* [Stack Overflow](https://stackoverflow.com/) was consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

[Back to top ⇧](#Dragon-Ball-Z-Text-Based-Combat-Game)

## Acknowledgements

* My mento, Marcel, for his genuine interest in my best end result and invaluable support and guidance. Truly would not have done it without him.

* My friend and piano tuner for his support and feedback throughout the project.

* My friends, for their valuable opinions and and critic during the design and development process.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.
