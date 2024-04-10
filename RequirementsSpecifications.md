<h1>Software Requirements Specifications<br>
for<br>
Snow Predictions</h1>

<h2> Version 1.0 approved<br>
<br>
Prepared by Frank Vanris, Conrad Nark,  Stefana Ciustea<br><br>
Bellevue College<br><br>
4/9/2024<br><br></h2>

<h2> 1. Introduction </h2><br><br>

**1.1 Problem statement**<br><br>
*To improve upon lack lustered predictions of next day snow fall.*<br><br>

**1.2 Summary**<br><br>
*To help and benefit the users in a way where the data is valid and that we can easily predict snow fall and give data immediately to the user with no problems. We also care about improving the users experiene when it comes to retrieving data and seeing the data projected to them.*<br><br>

**<h3>1.3 Product Scope</h3>**<br><br>
**1.3.1 In scope**<br>
* *user will be able to access data within an interface and see predicted data of current day information about snow fall.*<br>
* *An example would be when a user wants to go to snowqualmie pass to ski but doesn't know how snowy it is, or if it's going to snow more the next day. They can use this software to check the predicted growth in snow if there will be snow growth to see if tomorrows a good day to ski.*<br><br>

**1.3.2 Out of scope**<br><br>
* *Checking the outcomes of monthly data & seasonal data will not meet the requirements for this software.*<br>
* *Accessing past data from countless years for predictions will not meet the requirements for this software.*<br>
* *An app used within a mobile device will not meet the requirements for this software.*<br><br>

**<h3>1.4 References</h3>**<br>
Here are the given links to certain documents and websites that will guide us for this software:<br><br>
links:<br><br>
**Data**:
* https://nwac.us/data-portal/location/snoqualmie-pass/<br>
* https://api.weather.gov/points/47.3923,-121.4001<br>
* https://www.weather.gov/documentation/services-web-api<br>
* https://www.weather.gov/wrh/timeseries?site=SNO30<br><br>

**Learning Models**:<br>
* https://randomresearchai.medium.com/how-to-make-a-knn-model-in-python-5f7625bc1ab<br>
* https://www.ibm.com/topics/knn#:~:text=The%20k%2Dnearest%20neighbors%20(KNN)%20algorithm%20is%20a%20non,used%20in%20machine%20learning%20today.<br>
* https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html<br>
* https://www.ibm.com/topics/neural-networks<br>
* https://www.analyticsvidhya.com/blog/2022/01/introduction-to-neural-networks/
* https://towardsdatascience.com/machine-learning-for-beginners-an-introduction-to-neural-networks-d49f22d238f9<br><br>

**<h1>2. Overall Description**</h1><br>
**2.1 Compete analysis**<br>

| Top Competitor | Strengths | Weaknesses | Opportunities | Threats |
| --- | --- |--- |--- |--- |
| National Avalanche Services | - specialized expertise in avalanche prediction, which provides insights into snowfall patterns and potential avalanche risks; <br> <br> - deep understanding of local terrain and weather patterns in avalanche-prone areas, helping in more accurate predictions; <br> <br> - strong relationships with government agencies, ski resorts, and other stakeholders in the industry, having access to relevant data and resources; <br>| - primary focus on avalanche forecasting; | - collaboration with meteorological experts or technology companies to improve snowfall prediction abilities through modeling techniques; <br> <br> - development of partnerships with transportation companies, emergency response agencies, and other stakeholders to improve snowfall prediction accuracy and mitigate risks; <br> | - competition from specialized weather forecasting services or private companies offering advanced snowfall prediction tools; <br> <br> - climate change impacts leading to unpredictable weather patterns and potentially increased snowfall variability, challenging accurate prediction efforts |
| National Weather Services | | | | |
| | | | | |



**2.2 User Classes and Customer Profile**<br>

<5 W's (who, what, where, why, when, and how) about the intended users. Identify the various user classes
that you anticipate will use this product. User classes may be differentiated based on frequency of use, subset
of product functions used, technical expertise, security or privilege levels, educational level, or experience.
Describe the pertinent characteristics of each user class. Certain requirements may pertain only to certain
user classes. Distinguish the most important user classes for this product from those who are less important to
satisfy.> <br>

Intended Users: 
| Who | What | Where | Why | When | How |
| --- | --- |--- |--- |--- |--- |
| | | | | | |
| | | | | | |
| | | | | | |







**2.3 Design and Implementation Constraints**<br>

<Describe any items or issues that will limit the options available to the developers. These might include
corporate or regulatory policies; hardware limitations (timing requirements, memory requirements);
interfaces to other applications; specific technologies, tools, and databases to be used; parallel operations;
language requirements; communications protocols; security considerations; design conventions or
programming standards (for example, if the customer’s organization will be responsible for maintaining the
delivered software).>

**2.4 Assumptions and Dependencies**<br>

<List any assumed factors (as opposed to known facts) that could affect the requirements stated in the SRS.
These could include third-party or commercial components that you plan to use, issues around the
development or operating environment, or constraints. The project could be affected if these assumptions are
incorrect, are not shared, or change. Also identify any dependencies the project has on external factors, such
as software components that you intend to reuse from another project, unless they are already documented
elsewhere (for example, in the vision and scope document or the project plan).>

**<h1>3. Specific Requirements**</h1><br>

**3.1 User Interfaces**<br>

< Screenshots of feature UI design and descriptions, including why large or small screen. Describe the logical
characteristics of each interface between the software product and the users. This may include sample screen
images, any GUI standards or product family style guides that are to be followed, screen layout constraints,
standard buttons, and functions (e.g., help) that will appear on every screen, keyboard shortcuts, error
message display standards, and so on. Define the software components for which a user interface is needed.
Details of the user interface design should be documented in a separate user interface specification.>

**3.2 Functional Requirements**<br>

<This template illustrates organizing the functional requirements for the product by system features, the major
services provided by the product. You may prefer to organize this section by use case, mode of operation, user
class, object class, functional hierarchy, or combinations of these, whatever makes the most logical sense for
your product.>

**3.3 Logical Database Requirements**<br>
< what type of data they project needs to collect and keep track of it. List the main entities and fields you need for each>

**3.4 Performance and Software Quality Requirements**<br>
<If there are performance requirements for the product under various circumstances, state them here and
explain their rationale, to help the developers understand the intent and make suitable design choices. Specify
the timing relationships for real time systems. Make such requirements as specific as possible. You may need
to state performance requirements for individual functional requirements or features. Specify any additional
quality characteristics for the product that will be important to either the customers or the developers. Some to
consider are adaptability, availability, correctness, flexibility, interoperability, maintainability, portability,
reliability, reusability, robustness, testability, and usability. Write these to be specific, quantitative, and
verifiable when possible. At the least, clarify the relative preferences for various attributes, such as ease of use
over ease of learning.>

**<h1>4. Breakdown of work/Project timeline plan**</h1><br>

<How is the app being built? Who's doing the work?
Collect a numbered list of the project user stories (to be determined) references that remain in the SRS so they
can be tracked to closure> 

<br>

| User Story | Millstone | Assigned to: |
| --- | --- | --- |
| Req. 1: Gathering historical snowfall data | M1 | Frank | 
| Req. 2: K Nearest Neighbor modeling | M2  |  Conrad  |   
| Req. 3: Front End/ UI Design | M3  | Stefana |






