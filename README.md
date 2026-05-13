API Automation Project: Weather Service Suite
System Architecture
This framework is built using a Service Object Model (SOM). By decoupling the connection logic from the test cases, the suite remains maintainable, readable, and resilient to API and UI changes.

Framework Components
Base Connection Layer: Utilizes requests.Session() to manage persistent connections. This enables connection pooling, which reduces the overhead of re-establishing TCP connections across a large test suite.

Service Layer: Encapsulates specific endpoint logic (e.g., city-name lookups vs. ZIP-based queries). This abstraction ensures that tests do not need to know the internal URL structure or authentication requirements.

Contract Validation: Integrated Pydantic models to enforce strict schema validation. This ensures nested JSON responses maintain type integrity, protecting against "silent" regressions.

Cross-Platform UI Validation: Includes parallel UI test implementations using Selenium and Playwright. This side-by-side architecture allows for objective performance benchmarking, analyzing execution speed and "flakiness" in containerized environments.

Design Decisions
Why Pydantic? Standard assertions often only verify a single value. Pydantic allows us to validate the entire Data Contract—ensuring that if a temperature field suddenly changes from a float to a string, the test fails immediately.

Selenium vs. Playwright: By contrasting Selenium’s legacy WebDriver approach with Playwright’s modern event-driven architecture, the suite demonstrates a deep understanding of evolving industry standards and the ability to migrate legacy test debt.

Authentication Handling: API keys are injected into the session parameters at the base level. This eliminates the need to pass credentials into individual test methods, adhering to the DRY principle.

Testing Strategy
Data-Driven Execution: Utilized @pytest.mark.parametrize to execute a single test logic across multiple geographic coordinates, ensuring consistent coverage with minimal code bloat.

Negative Testing & Security: Implemented targeted negative test cases to verify the framework's handling of 401 Unauthorized responses. This ensures the system correctly identifies and reports authentication failures rather than throwing unhandled exceptions.

Headless Execution: Engineered the UI suite to run in a "headless" state, optimized for Linux-based CI/CD runners.

CI/CD Integration: Powered by GitHub Actions. The suite executes on every push to main, pulling sensitive credentials from GitHub Secrets to maintain security best practices.

Project Structure
Plaintext
├── .github/workflows/    # CI/CD Pipeline configuration
├── api_objects/          # Service Object Layer (BaseClient & WeatherService)
├── models/               # Pydantic Data Models (Contract Validation)
├── tests/                # API Test suites (Positive & Negative)
├── ui_tests/             # UI Comparison suite (Selenium & Playwright)
├── requirements.txt      # Project dependencies
└── .env.example          # Template for required environment variables
Setup & Installation
1. Clone and Install
Bash
git clone https://github.com/raj469-doit/weather-api-automation.git
cd weather-api-automation
pip install -r requirements.txt
playwright install  # Required for Playwright UI tests
2. Environment Configuration
Locate the .env.example file and rename it to .env. Add your OpenWeatherMap API key:

Plaintext
OPENWEATHER_API_KEY=your_actual_key_here
Execution
Run all tests (API & UI):

Bash
python3 -m pytest -v
Run specific suites:

Bash
# Run only API tests
python3 -m pytest tests/ -v

# Run UI comparison tests
python3 -m pytest ui_tests/ -v -s
Roadmap & Scalability
Parallel Execution: Integration of pytest-xdist to decrease execution time as the suite grows.

Mocking: Implementing a mocking library to simulate 500-series server errors without relying on the live provider.

Advanced Reporting: Integration of Allure for better stakeholder visibility into test results.