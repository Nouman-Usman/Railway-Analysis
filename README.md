## Railway Analysis

The Railway Analysis is a comprehensive application designed to manage railway schedules, bookings,
and user feedback. The system integrates data structures and algorithms to provide efficient solutions
for scheduling, route verification, and user feedback processing. The graphical user interface (GUI) is
built using PySide2, providing an intuitive and user-friendly experience.

[Key Features]():

1. User Authentication and Signup:

Prioritizing security, the system implements a multi-layered approach to user authentication. User credentials, stored in a local CSV database, are encrypted using the bcrypt library for enhanced protection against potential data breaches. Unique usernames and email addresses further strengthen security and ensure individual identification.

2. Google Sign-In Integration:

Enhancing user convenience, the system seamlessly integrates Google sign-in using the OAuth2.0 protocol. This allows users to quickly access their accounts without the need to create and remember new passwords. Asynchronous management of the sign-in process ensures a smooth and responsive user experience.
Railway Schedule Management:

The system efficiently manages railway schedules by extracting information from a CSV file named "Train and Time.csv." Utilizing a linked list data structure, the extracted schedule data is dynamically organized, enabling efficient storage and retrieval. The user-friendly interface includes a sortable table and dynamic combo boxes for interactive filtering and exploration of schedules based on user-specified criteria.

3. Booking Confirmation:

To ensure accurate bookings, the system incorporates an outstanding constraint checking mechanism. Before finalizing a booking, the system verifies that the selected start and end locations align with existing routes within the railway network, preventing invalid journeys. Transparent pricing calculations are performed based on ticket types and quantities chosen by the user.

4. Graph Visualization:

Visualizing the intricate relationships within the data, the system harnesses the power of graph visualization. Essential graph attributes are extracted from a file named "graphAttributes.txt," serving as blueprints for constructing a visual representation of the graph using the NetworkX and Matplotlib libraries.

5. User Feedback:

Actively encouraging user feedback, the system facilitates the collection and organization of user-provided feedback. Feedback is stored within a stack data structure named "feedback-stack" and persistently saved to a dedicated file named "feedback.txt" for long-term accessibility and analysis.

## Acknowledgements

We extend our sincere gratitude to everyone who contributed to the successful completion of the Railway Analysis project. This endeavor would not have been possible without the dedication and support of the following individuals:

## Project Team

Nouman Usman, Shahbaz Ghafil and Khuram Iqbal: Thank you to our collaborators for their valuable insights, ideas, and collaborative efforts that enriched the project.

# Mentors and Advisors
Mr.Nazeef-Ul-Haq: Your guidance and mentorship provided invaluable direction, helping us navigate challenges and refine our project goals.


UET Lahore: We express our gratitude to our educational institution for providing an environment conducive to learning and innovation.
This project was a collaborative effort, and each person mentioned above played a crucial role in its success. Thank you for your dedication, expertise, and support.

## Authors

- [Nouman](https://github.com/Nouman-Usman)
- [Shahbaz](https://github.com/ShahbazShaddy)
- [Khuram](https://github.com/khuramgill)


## Environment Variables

To run this project, you will need to download python 3.9 and add the following environment variables to your .env file
Yours will be change from mine:

`C:\Users\Nouman\AppData\Local\Programs\Python\Python39\Scripts\`

`C:\Users\Nouman\AppData\Local\Programs\Python\Python39\`

After updating the .env variables you need to tun the following command in your powershell

pip install -r requirements.txt


## Documentation

[Documentation](https://www.overleaf.com/read/svpcyjhhhnks#d5f951)


