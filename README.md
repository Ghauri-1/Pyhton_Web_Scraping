# Pyhton Web Scraping Automation Bot
*Automated Facebook interaction tool using Python and Selenium.*


You have to first create a facecbook account and change the credentials in the code. 


##  Overview
This project is an automated interaction bot designed for research and educational purposes. It features login automation, dynamic DOM handling for changing Facebook layouts, and human-like typing to demonstrate timing and interaction strategies in automated web testing, simulating real user behavior.

##  Key Features
* **Automated Login**: Securely handles authentication.
* **Smart DOM Handling**: Uses dynamic waits to interact with elements regardless of load speed.
* **Human-like Interaction**: Implements randomized delays and typing speeds to mimic human behavior.
* **Error Recovery**: Basic exception handling for element time-outs or page changes.

##  Tech Stack
* **Language**: Python 3.x
* **Automation**: [Selenium WebDriver](https://www.selenium.dev)
* **Browser**: Chrome (via ChromeDriver)

##  Setup & Installation
1. **Clone the repo**: `git clone https://github.com`
2. **Install dependencies**: `pip install selenium`
3. **Configure Credentials**: 
   - Create a `.env` file in the root directory.
   - Add your credentials: `FB_EMAIL=your_email`, `FB_PASS=your_password`.
4. **Run the script**: `python main.py`

##  Important Point to Notice / Disclaimer
This project is strictly for **educational and research purposes**. Using automation tools on Facebook may violate their [Terms of Service](https://www.facebook.com). The author is not responsible for any account suspensions or consequences resulting from the use of this software.

##  Future Improvements
- [ ] Implement headless browser mode for faster execution.
- [ ] Add proxy rotation support to avoid IP flagging.
- [ ] Develop a GUI for easier credential management.
