<div align="center">
    <h1>【 Project Based ROS NOETIC 】</h1>
    <h3></h3>
</div>

<details>
  <summary> Description </summary>

In the fictional country of Singanesia, there are only two providers for sending data, each sending data as follows:

- Provider SmartGuys: Sends data of type std_msgs/String Message with three possibilities only ("LOW", "MEDIUM", "HIGH") Documentation
- Provider XS: Sends data of type std_msgs/Int16 Message with values ranging from 0 to 100 Documentation
When these two providers send data, there's a user named Budi who wants to consume the data for his device. Upon receiving the data, there are several conditions:

- If Provider SmartGuys sends "HIGH" and Provider XS sends a value > 50, Budi will display "LANCAR".
- If Provider SmartGuys sends "MEDIUM" and Provider XS sends a value > 50, Budi will display "PATAH-PATAH".
- If Provider SmartGuys sends "LOW" and Provider XS sends a value > 50, Budi will display "NGE-LAG".
- Otherwise, Budi will display "MENDING TURU".
</details>
<details>
  <summary> Setup </summary>

- Clone this repository to your local machine.
- Make sure you have ROS Noetic installed and configured properly.
- Navigate to the directory containing the ROS nodes.
- Build the ROS package using 'catkin_make'.
- Run the ROS nodes using 'rosrun' command.

<details>

**Output code**
![Output Images](Images/Output.png)

