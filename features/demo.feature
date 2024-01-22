Feature: User journeys on the Sauce Demo website

  # Scenario: The user can log in with a valid password
  #  Given I am on the Sauce Demo login page
  #   When I enter user name "standard_user" and a valid password
  #    And I click the "login-button"
  #   Then I should be taken to the inventory page

  Scenario Outline: The user can add multiple items to their basket
   Given I log on to the inventory page
     And I have a list of 'items' to order
    # When I click 'Add to cart' for each item
    #  And I click the "shopping_cart_link"
    # Then I should see my items in the checkout page 
   Examples:
   | items                                                                            |
   | Sauce Labs Backpack, Sauce Labs Bike Light                                       | 
  #  | Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie             |  
