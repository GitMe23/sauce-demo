Feature: User journeys on the Sauce Demo website

  @sauce-001 @browser
  Scenario: The user can log in with a valid password
   Given I am on the Sauce Demo login page
    When I enter user name "standard_user" and a valid password
     And I click the "login-button"
    Then I should be taken to the "inventory" page

  @sauce-002 @browser
  Scenario Outline: The user can add a number of items to their basket
   Given I log on to the inventory page
     And I have a list of <items> to order
    When I click 'Add to cart' for each item
     And I click the "shopping_cart_container"
    Then I should be taken to the "cart" page 
     And I should see all of my items 
   Examples: Add items to cart 
   | items                                                                   |
   | Test.allTheThings() T-Shirt (Red)                                       | 
   | Sauce Labs Backpack, Sauce Labs Bike Light                              | 
   | Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie    |  
