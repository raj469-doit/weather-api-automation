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



Selenium vs. Playwright: By contrasting Selenium's legacy WebDriver approach with Playwright's modern event-driven architecture, the suite demonstrates a deep understanding of evolving industry standards and the ability to migrate legacy test debt.



Authentication Handling: API keys are injected into the session parameters at the base level. This eliminates the need to pass credentials into individual test methods, adhering to the DRY principle.

Testing Strategy

Data-Driven Execution: Utilized @pytest.mark.parametrize to execute a single test logic across multiple geographic coordinates, ensuring consistent coverage with minimal code bloat.



Negative Testing \& Security: Implemented targeted negative test cases to verify the framework's handling of 401 Unauthorized responses. This ensures the system correctly identifies and reports authentication failures rather than throwing unhandled exceptions.



Headless Execution: Engineered the UI suite to run in a "headless" state, optimized for Linux-based CI/CD runners.



CI/CD Integration: Powered by GitHub Actions. The suite executes on every push to main, pulling sensitive credentials from GitHub Secrets to maintain security best practices.

Project Structure

├── .github/workflows/    # CI/CD Pipeline configuration



├── api\_objects/          # Service Object Layer (BaseClient \& WeatherService)



├── models/               # Pydantic Data Models (Contract Validation)



├── tests/                # API Test suites (Positive \& Negative)



├── ui\_tests/             # UI Comparison suite (Selenium \& Playwright)



├── requirements.txt      # Project dependencies



└── .env.example          # Template for required environment variables

Prerequisites

Python 3.10+ (tested on 3.12 and 3.13)

Git

pip

An OpenWeatherMap API key (free tier works)

Setup \& Installation

1\. Clone and Install

Linux / macOS:



git clone https://github.com/raj469-doit/weather-api-automation.git



cd weather-api-automation



pip install -r requirements.txt



playwright install  # Required for Playwright UI tests



Windows (PowerShell):



git clone https://github.com/raj469-doit/weather-api-automation.git



cd weather-api-automation



python -m venv venv



.\\venv\\Scripts\\Activate.ps1



pip install -r requirements.txt



playwright install



Note: If activating the virtual environment fails with an execution-policy error, run the following once:



Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

2\. Environment Configuration

Locate the .env.example file and rename it to .env. Add your OpenWeatherMap API key:



OPENWEATHER\_API\_KEY=your\_actual\_key\_here

Execution

Run all tests (API \& UI):



python3 -m pytest -v



Run specific suites:



\# Run only API tests



python3 -m pytest tests/ -v



\# Run UI comparison tests



python3 -m pytest ui\_tests/ -v -s



Windows note: Use python instead of python3. The UI tests were designed for headless Linux CI runners; when running locally on Windows, Selenium and Playwright will open visible browser windows rather than running headless. This is expected behavior.

Compatibility Notes

Python 3.13 on Windows: The pydantic dependency is pinned to >=2.5.2 (rather than an exact version) because pydantic-core==2.14.5 has no prebuilt wheel for Python 3.13 on Windows. Without a prebuilt wheel, pip attempts to compile from Rust source, which requires the MSVC linker (link.exe) from Visual Studio Build Tools. The loosened pin allows pip to resolve a newer version with a compatible prebuilt wheel.

Anaconda users: If your virtual environment was created with an Anaconda-managed Python, verify the venv is properly isolated by running python -c "import sys; print(sys.prefix)" — the output should point inside your project's venv/ folder, not into an anaconda3 directory.

Roadmap \& Scalability

Parallel Execution: Integration of pytest-xdist to decrease execution time as the suite grows.



Mocking: Implementing a mocking library to simulate 500-series server errors without relying on the live provider.



Advanced Reporting: Integration of Allure for better stakeholder visibility into test results.





