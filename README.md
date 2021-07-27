# HuggingArtists - Train a model to generate lyrics

<img src="img/logo.jpg" width="420" align="center">

_Disclaimer: this project is not to be used to publish any false generated information but to perform research on Natural Language Generation._

## How to use

To test the demo, click on below link and share your results!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlekseyKorshuk/huggingartists/blob/master/huggingartists-demo.ipynb)

You can also use it locally by installing the dependencies with `pipenv` or `pip` and use [`huggingartists-demo.ipynb`](huggingartists-demo.ipynb)

## Results

There are some interesting lyrics. Contact me to add your results:

#### Eminem:
~~~
I am a bit of a nutter
Like a fucking crazy nut
But I just wanted to break and get a little more serious, so be patient
I dont think I need no medical attention
But I do know that these niggas gonna be in my prayers
And they say Im a nutter
Like a fucking crazy nut
But I love you
I am a nutter
Like a fuckin nutter
But I feel like the greatest that I can be
With your body and your spirits
But I dont know how I will act
When I finally get out
And I get pissed off
Ill be right back at ya with the first one on the floor
But I aint ever gonna get the respect youve been getting
And Im a nutter
~~~

#### Drake:
~~~
My dream is just another night, I have to sleep
Like I say
I say, I know you dont love me if you've been waiting
Just say
Hey, what we have is not an answer
Yeah... just talk
I say
Yeah... Ima get it
I go crazy
I know we gonna be here next, yeah...
Got my body back
Lights on the ceiling
Hangin in my room, I want somebody to put me right there
And I couldnt go wrong
No... I know, I know, yeah...
I dont wanna die, but...
I just wanna be here, I need somebody to put me right there
And I couldnt go wrong
No... I cant ever go wrong, I cant never
~~~

### Check existing:
* [Models](https://huggingface.co/models?filter=huggingartists)
* [Datasets](https://huggingface.co/datasets?filter=huggingartists)



## Features:
* Generate lyrics by a specific artist
* Automatically upload models and datasets to [HuggingFace Profile](https://huggingface.co/huggingartists) after each each run
* Parse dataset once and use it next time without spending time
* Each next run by any person will resume training from checkpoint
* Training and results are automatically logged into [W&B](https://docs.wandb.com) through the [HuggingFace integration](https://docs.wandb.com/huggingface)


## About

*Built by Aleksey Korshuk*

[![Follow](https://img.shields.io/github/followers/AlekseyKorshuk?style=social)](https://github.com/AlekseyKorshuk)

For more details, visit the project repository.

[![GitHub stars](https://img.shields.io/github/stars/AlekseyKorshuk/huggingartists?style=social)](https://github.com/AlekseyKorshuk/huggingartists)
