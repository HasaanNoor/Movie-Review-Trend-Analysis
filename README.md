# Movie Review Trend Analysis (1970-2024)

## Description

This project aims to analyze movie review data from Rotten Tomatoes spanning from 1970 to 2024. The analysis includes various metrics such as polarity, subjectivity, and sentiment trends over the years. The project also involves web scraping to gather review data from Rotten Tomatoes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To use this project, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/HasaanNoor/Movie-Review-Trend-Analysis.git
cd Movie-Review-Trend-Analysis
# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Analysis

1. Ensure you have followed the installation instructions.
2. Place your datasets in the `data` directory.
3. Run the web scraping script to fetch reviews from Rotten Tomatoes:
   ```bash
   python scripts/scrape_reviews.py
   ```
4. Run the analysis script:
   ```bash
   python scripts/analyze_reviews.py
   ```

### Customizing the Analysis

- You can modify the `scrape_reviews.py` script to add more movie URLs.
- You can modify the `analyze_reviews.py` script to change the analysis parameters.

## Data

The data used in this project includes:
- Movie reviews from Rotten Tomatoes.
- Movie metadata such as release dates, genres, and ratings.

## Scripts

- `analyze_reviews.py`: Script for analyzing and visualizing the Rotten Tomatoes review data, including polarity, subjectivity, and sentiment analysis.
- `scraping.py`: Script for scraping reviews from Rotten Tomatoes.

## Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Create a new Pull Request.

## Contact

Hasaan Noor - [hasaan.noor@outlook.com](mailto:hasaan.noor@outlook.com)

Project Link: [https://github.com/HasaanNoor/Movie-Review-Trend-Analysis](https://github.com/HasaanNoor/Movie-Review-Trend-Analysis)
