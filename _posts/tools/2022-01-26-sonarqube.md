最快上手

# 軟件

docker

# 步驟

安裝配置

```bash
#docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 0.0.0.0:9000:9000 sonarqube:latest
#用container station下載sonarqube
#用橋接模式進入
#瀏覽器打開http://192.168.1.130:9000
#賬號密碼都是admin
```

分析代碼

我選擇的是local，按照他的指引，需要下載程序到本地，然後執行

```bash
F:\_codes\mypipe>F:\Users\cutepig\Downloads\sonar-scanner-cli-4.6.2.2472-windows\sonar-scanner-4.6.2.2472-windows\bin\sonar-scanner.bat  -D"sonar.projectKey=myalgcodes" -D"sonar.sources=." -D"sonar.host.url=http://192.168.1.132:9000" -D"sonar.login=e8618d8be64b2b94d57459c2e509d3346ebc0e6d"
INFO: Scanner configuration file: F:\Users\cutepig\Downloads\sonar-scanner-cli-4.6.2.2472-windows\sonar-scanner-4.6.2.2472-windows\bin\..\conf\sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 4.6.2.2472
INFO: Java 11.0.11 AdoptOpenJDK (64-bit)
INFO: Windows 10 10.0 amd64
INFO: User cache: C:\Users\cutepig\.sonar\cache
INFO: Scanner configuration file: F:\Users\cutepig\Downloads\sonar-scanner-cli-4.6.2.2472-windows\sonar-scanner-4.6.2.2472-windows\bin\..\conf\sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: Analyzing on SonarQube server 9.2.4
INFO: Default locale: "zh_CN", source code encoding: "GBK" (analysis is platform dependent)
INFO: Load global settings
INFO: Load global settings (done) | time=267ms
INFO: Server id: BF41A1F2-AX6WygBPN7Kjfeyf4FXw
INFO: User cache: C:\Users\cutepig\.sonar\cache
INFO: Load/download plugins
INFO: Load plugins index
INFO: Load plugins index (done) | time=93ms
INFO: Load/download plugins (done) | time=243ms
INFO: Process project properties
INFO: Process project properties (done) | time=18ms
INFO: Execute project builders
INFO: Execute project builders (done) | time=5ms
INFO: Project key: myalgcodes
INFO: Base dir: F:\_codes\mypipe
INFO: Working dir: F:\_codes\mypipe\.scannerwork
INFO: Load project settings for component key: 'myalgcodes'
INFO: Load project settings for component key: 'myalgcodes' (done) | time=91ms
INFO: Load quality profiles
INFO: Load quality profiles (done) | time=168ms
INFO: Load active rules
INFO: Load active rules (done) | time=14485ms
INFO: Indexing files...
INFO: Project configuration:
INFO: 41 files indexed
INFO: 1211 files ignored because of scm ignore settings
INFO: Quality profile for json: Sonar way
INFO: Quality profile for py: Sonar way
INFO: ------------- Run sensors on module myalgcodes
INFO: Load metrics repository
INFO: Load metrics repository (done) | time=130ms
INFO: Sensor Python Sensor [python]
WARN: Your code is analyzed as compatible with python 2 and 3 by default. This will prevent the detection of issues specific to python 2 or python 3. You can get a more precise analysis by setting a python version in your configuration via the parameter "sonar.python.version"
INFO: Starting global symbols computation
INFO: 24 source files to be analyzed
INFO: Load project repositories
INFO: Load project repositories (done) | time=57ms
INFO: 24/24 source files have been analyzed
INFO: Starting rules execution
INFO: 24 source files to be analyzed
INFO: 24/24 source files have been analyzed
INFO: Sensor Python Sensor [python] (done) | time=11487ms
INFO: Sensor Cobertura Sensor for Python coverage [python]
INFO: Sensor Cobertura Sensor for Python coverage [python] (done) | time=245ms
INFO: Sensor PythonXUnitSensor [python]
INFO: Sensor PythonXUnitSensor [python] (done) | time=260ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: 'sonar.coverage.jacoco.xmlReportPaths' is not defined. Using default locations: target/site/jacoco/jacoco.xml,target/site/jacoco-it/jacoco.xml,build/reports/jacoco/test/jacocoTestReport.xml
INFO: No report imported, no coverage information will be imported by JaCoCo XML Report Importer
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=16ms
INFO: Sensor IaC CloudFormation Sensor [iac]
INFO: 0 source files to be analyzed
INFO: 0/0 source files have been analyzed
INFO: Sensor IaC CloudFormation Sensor [iac] (done) | time=122ms
INFO: Sensor CSS Rules [javascript]
INFO: No CSS, PHP, HTML or VueJS files are found in the project. CSS analysis is skipped.
INFO: Sensor CSS Rules [javascript] (done) | time=4ms
INFO: Sensor C# Project Type Information [csharp]
INFO: Sensor C# Project Type Information [csharp] (done) | time=2ms
INFO: Sensor C# Analysis Log [csharp]
INFO: Sensor C# Analysis Log [csharp] (done) | time=33ms
INFO: Sensor C# Properties [csharp]
INFO: Sensor C# Properties [csharp] (done) | time=1ms
INFO: Sensor JavaXmlSensor [java]
INFO: Sensor JavaXmlSensor [java] (done) | time=3ms
INFO: Sensor HTML [web]
INFO: Sensor HTML [web] (done) | time=13ms
INFO: Sensor VB.NET Project Type Information [vbnet]
INFO: Sensor VB.NET Project Type Information [vbnet] (done) | time=3ms
INFO: Sensor VB.NET Analysis Log [vbnet]
INFO: Sensor VB.NET Analysis Log [vbnet] (done) | time=31ms
INFO: Sensor VB.NET Properties [vbnet]
INFO: Sensor VB.NET Properties [vbnet] (done) | time=0ms
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=105ms
INFO: SCM Publisher SCM provider for this project is: git
INFO: SCM Publisher 24 source files to be analyzed
INFO: SCM Publisher 24/24 source files have been analyzed (done) | time=1844ms
INFO: CPD Executor 9 files had no CPD blocks
INFO: CPD Executor Calculating CPD for 15 files
INFO: CPD Executor CPD calculation finished (done) | time=42ms
INFO: Analysis report generated in 327ms, dir size=209.9 kB
INFO: Analysis report compressed in 2470ms, zip size=77.2 kB
INFO: Analysis report uploaded in 123ms
INFO: ANALYSIS SUCCESSFUL, you can browse http://192.168.1.132:9000/dashboard?id=myalgcodes
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://192.168.1.132:9000/api/ce/task?id=AX6XCf7QP7bi5AcfKa6f
INFO: Analysis total time: 39.080 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 41.568s
INFO: Final Memory: 9M/37M
INFO: ------------------------------------------------------------------------
```

發現默認不支持cpp代碼，還需要折騰半天，還是依賴于cppcheck，如果這樣，我乾脆直接使用cppcheck了。最終放棄

# 參考

https://docs.sonarqube.org/latest/setup/get-started-2-minutes/

