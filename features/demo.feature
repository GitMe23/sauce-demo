Feature: User journeys on the Sauce Demo website

  @sauce-001 @browser
  Scenario: The user can log in with a valid password
   Given I am on the Sauce Demo login page
    When I enter user name "standard_user" and a valid password
     And I click "login-button"
    Then I should be taken to the "inventory" page

  @sauce-002 @browser
  Scenario Outline: The user can add a number of items to their basket
   Given I log on to the inventory page
     And I have a list of <items> to order
    When I click 'Add to cart' for each item
     And I click "shopping_cart_container"
    Then I should be taken to the "cart" page 
     And I should see all of my items 
   Examples: 
   | items                                                                   |
   | Test.allTheThings() T-Shirt (Red)                                       | 
   | Sauce Labs Backpack, Sauce Labs Bike Light                              | 
   | Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie    |

  @sauce-003 @browser
  Scenario Outline: The user can check out and enter their details
   Given I have a list of <items> to order
     And I am on the cart page
    When I click "checkout"
    Then I should be taken to the "checkout-step-one" page 
  Examples: 
   | items                                        |
   | Sauce Labs Backpack, Sauce Labs Bike Light   |

  # @sauce-004 @browser
  # Scenario Outline: The user can check out and enter their details
  #  Given I have a list of <items> to order
  #    And I am on the "checkout-step-one" page 
  #    And I enter my <first> name, <last> name, and <zip> 
  #   When I click "continue"
  #   Then I should be taken to the "checkout-step-two" page 
  #    And 
  # Examples: 
  #  | items                                        | first     | last    | zip     |
  #  | Sauce Labs Backpack, Sauce Labs Bike Light   | Joe       | Bloggs  | 101     |
   
   
   


