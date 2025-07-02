🌿 *These three projects are console-based, written in Python - expanding my understanding of data structures and scheduling logic using queues, stacks, and binary trees.*

# 1. Mini Trees Concept 🌳
This project explores how different tree traversal algorithms work using binary trees. It was built to practice recursive logic and visualize how data flows through a tree structure.

# Features
* **In-order Traversal**: Visit left subtree → root → right subtree
* **Pre-order Traversal**: Visit root → left subtree → right subtree
* **Post-order Traversal**: Visit left subtree → right subtree → root
* **Readable Outputs** for each traversal type


# 2. Hospital Appointment System 📅
A hospital scheduling system that organizes patient appointments across multiple days. Appointment times are auto-generated in **30-minute slots** starting from 9:00 AM, and queued based on the date provided.

# Features
* **Add Patients** with name, age, and preferred date
* **Auto-assign Time Slots** for each date
* **Organized Waitlist View** grouped by date
* **FIFO Queue Structure** ensures fair and timely booking
  

# 3. Doctor Appointment System 🩺
This appointment system handles requests, confirmations, cancellations, and rescheduling using a combination of **queues, stacks, and lists** to simulate a real clinic workflow.

# Features
* **Request Appointments**: Add patients to a waitlist (queue)
* **Confirm Appointments**: Move from waitlist to confirmed list
* **Cancel Appointments**: Track cancelled ones in a stack (LIFO)
* **Reschedule Appointments**: Update confirmed dates
* **View Lists**: Show confirmed and waiting patients

