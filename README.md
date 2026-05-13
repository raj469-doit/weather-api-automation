API Automation Project: Weather Service Suite
System Architecture
This framework is built using a Service Object Model (SOM). By decoupling the connection logic from the test cases, the suite remains maintainable, readable, and resilient to API changes.

Framework Components
Base Connection Layer: Utilizes requests.Session() to manage persistent connections. This enables connection pooling, which reduces the overhead of re-establishing TCP connections across a large test suite.

Service Layer: Encapsulates specific endpoint logic (e.g., city-name lookups vs. ZIP-based queries). This abstraction ensures that tests do not need to know the internal URL structure or authentication requirements.

Contract Validation: Integrated Pydantic models to enforce strict schema validation. This ensures nested JSON responses maintain type integrity, protecting against "silent" regressions where data types change but status codes remain 200.

Design Decisions
Why Pydantic? Standard assertions often only verify a single value (e.g., city == "London"). Pydantic allows us to validate the entire Data Contract—ensuring that if a temperature field suddenly changes from a float to a string, the test fails immediately.

Authentication Handling: API keys are injected into the session parameters at the base level. This eliminates the need to pass credentials into individual test methods, adhering to the DRY (Don't Repeat Yourself) principle.

Testing Strategy
Data-Driven Execution: Utilized @pytest.mark.parametrize to execute a single test logic across multiple geographic coordinates, ensuring consistent coverage with minimal code bloat.

CI/CD Integration: Powered by GitHub Actions. The suite executes on every push to main, pulling sensitive API credentials from GitHub Secrets to maintain security best practices.

Project Structure
Plaintext
├── .github/workflows/    # CI/CD Pipeline configuration
├── api_objects/         # Service Object Layer (BaseClient & WeatherService)
├── models/               # Pydantic Data Models (Contract Validation)
├── tests/                # Positive, Negative, and Data-Driven test suites
├── requirements.txt      # Project dependencies
└── .env.example          # Template for required environment variables
Setup & Installation
1. Clone and Install
Bash
git clone https://github.com/raj469-doit/weather-api-automation.git
cd weather-api-automation
pip install -r requirements.txt
2. Environment Configuration
The project uses a .env file for local development. A template is provided in the repository.

Locate the .env.example file.

Rename it to .env: mv .env.example .env (or copy it).

Add your OpenWeatherMap API key to the file:

Plaintext
OPENWEATHER_API_KEY=your_actual_key_here
Execution
To run the full suite with verbose output:

Bash
python3 -m pytest -v
To run and generate a self-contained HTML report:

Bash
python3 -m pytest -v --html=report.html --self-contained-html
Roadmap & Scalability
Parallel Execution: Integration of pytest-xdist to decrease execution time as the suite grows.

Mocking: Implementing a mocking library to simulate 500-series server errors and edge cases without relying on the live provider.

Advanced Reporting: Integration of Allure for better stakeholder visibility into test results.