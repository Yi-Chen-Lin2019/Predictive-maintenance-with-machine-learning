# Problem statement
Machines are critical to all business nowadays, and we expect them to operate at peak level for long time. Normally, we can use corrective maintenance strategy to make the best use of machines. But we could end up costing even higher due to downtime and labor.

Preventive maintenance comes in to reduce unplanned failures while businesses try to address problem in advance. However, the costs could still be high. By using predictive maintenance, we can prevent those unexpected problems more efficiently. We can fix the machines just in time as we monitor and predict the status of them.

In this project, predictive maintenance is the main concept. There are two aspects to do the predictive maintenance in this project, supervised and unsupervised learning. In supervised learning, predicting remaining useful life and failure prediction are the goals. While in unsupervised learning, detecting anomalies of the machine is the target. Python and its machine learning related libraries are the main tools in this project. The solution of this project could help industry to lower the chance of unexpected downtime and reduce costs.

# Aims and objectives
The aim of this project is to propose machine learning solutions for predictive maintenance in responds to Industry 4.0. There are three tasks proposed:
* Anomaly detection: The model should be able to detect the anomalies within data.
* Remaining useful life prediction: The model should be able to predict the remaining useful life of a machine to help people be prepared for maintenance or replacement.
* Failure prediction: The model should be able to predict whether there will be a failure.

# Data source
There are two datasets used in this project:
* Bearing: Both anomaly detection and failure prediction use bearing dataset which is provided by [Case School of Engineering Bearing Data Center](https://engineering.case.edu/bearingdatacenter/download-data-file) and downloaded from [lestercardoz11’s public GitHub repository](https://github.com/lestercardoz11/fault-detection-for-predictive-maintenance-in-industry-4.0.git).
* Battery: Remaining useful life (RUL) task use battery dataset which is downloaded from [NASA](http://ti.arc.nasa.gov/project/prognostic-data-repository) and battery B0005 is chosen as study object.