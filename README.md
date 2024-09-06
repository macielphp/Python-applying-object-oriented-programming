# Python-applying-object-oriented-programming
 Project initialized by the course "Python: aplicando a Orientação a Objetos" from Alura


## Logic
Look, I want to add some new business rules to the project started by the course.

0. Need to add restaurant names and categories.

1. First, I have to choose what restaurant(s) are/is open(True) ou closed(False).

    1.1. Let's suppose, Fips is open(true)
    
        1.1.1. Must add members to the restaurant's team.

            1.1.2. Now there are Bruno, Marcos and Pedro. But only Marcos is working(Status = True). 

                1.1.2.1. A customer entered the restaurant and Marcos made some question: what's his/her name? Julia. Which table number do you choose? 3. As there is only Marcos(only he appears as option on the system to attend) working, so Marcos will be the attendant and cashier as it is up to Marcos to charge the customer. As Marcos started, he will also end.So, only Marcos is responsible for that customer named Julia and her escorts. If another customer has got into the restaurant, Marcos could be the attendent and cashier of two tables's number.
    
    
                    1.1.2.1.1. The attendent Marcos let the menu(not integrate to the system) to Julia choose the food. As the customers chooses their food, they call Marcos, and Marcos take notes on his tablet which is integrated has an app integrated to the system.

                        1.1.2.1.1.1. The system sum the costs based on what food the customers choose. The customers are now enjoy their food. "Bill's paid' status" is False at the moment.

                            1.1.2.1.1.1.1. Now, the customer has already eaten and owns 499 to the cashier. They decided to pay and rate the restaurant. Then, they leaved it. Now the "Bill's paid' status" is True and Marcos is not responsible of the table number 1 until he attend another customer in the same table.
    
    1.2. If a restaurant has no ratings given by customers, then the rating of it has to start with 5 in order to motivate potencial customers, instead of starting with rating 0.
    
