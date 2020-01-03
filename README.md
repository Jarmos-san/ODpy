# ODpy

**The project has been ARCHIVED INDEFINITELY until for notice due to the developer account being put behind a pay wall. I apologise for the inconvenience caused, if any. I was ambitious about the project but unfortunately I don't have the means to pay for the project yet as of now. Although unlikely, but I might come back to this project once again if/when I can afford to pay for it's use.**

A simple Python wrapper based on the latest [Oxford Dictionary API v2](https://api-blog.oxforddictionaries.com/2018/03/27/make-first-call-oxford-dictionaries-api/) written mainly as a resource for a project-based learning oppurtunity.

I haven't set out a long-term plan to build a full-blown Python library that could be used by many but as of now it's more of an Open-Source project for anyone to contribute to regardless of, if they are learning programming in general or want to teach Python to someone. As such while going through the source-code it might look like it has a lot of uncessary comments but the idea behind it is for someone who is new to Python or programming to general, to go through and read each line of code & get a fair idea of what a specific block of function or a class is supposed to be doing.

## Development

Follow the steps below to set up a quick development environment for testing locally on your system.

1. Check if you have Python3.7+ installed locally on your system using the `python --version` command.
2. Clone the repository locally using the `git clone https://github.com/Jarmos-san/ODpy.git` command.
3. Change directory into the local repository and run a virtual environment using the `python -m venv <MyVirtualEnvironmentName>`.
4. Activate the virtual environment by running the `source <MyVirtualEnvironmentName>/bin/activate`.
5. And then install the dependencies using pip by running `pip install -r requirements.txt`.
6. Sign in to a [Developer Account](https://developer.oxforddicionaries.com/) to get your API credentials [here](https://developer.oxforddictionaries.com/admin/applications)
7. Although it's highly preferred to set the API secret keys using the `export ID="<YouAppID>"` & `export KEY="<YourAppKey>"` for maintaining utmost security, a `config.ini` file can also be created manually with the following format.

```ini
[SECRET]
ID="<YourAppID>"
KEY="<YourAppKey>"
```

## License

Although I've licensed the source code under the terms & conditions of the [MIT LICENSE](https://github.com/Jarmos-san/OD.py/blob/master/LICENSE), I would like to point out that the main motive behind such was to set a project-based learning path. I have not thought far enough to make a commercially viable product, so please use the source code with discretion. Also it should be duly noted that the source code makes calls to an API hosted by the [Oxford University Press](https://academic.oup.com/journals) and strictly adheres to the ***Non-commercial T&Cs*** of their [Oxford Dictionary API](https://developer.oxforddictionaries.com/).

For further queries on specific use cases it's recommended that you reach out to their [support group](https://developer.oxforddictionaries.com/#).
