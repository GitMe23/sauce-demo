Feature: User journeys on the Sauce Demo website

  # @sauce-001 @browser
  # Scenario: The user can log in with a valid password
  #  Given I am on the Sauce Demo login page
  #   When I enter user name "standard_user" and a valid password
  #    And I click "login-button"
  #   Then I should be taken to the "inventory" page

  # @sauce-002 @browser
  # Scenario Outline: The user can add a number of items to their basket
  #  Given I log on to the inventory page
  #    And I have a list of <items> to order
  #   When I click 'Add to cart' for each item
  #    And I click "shopping_cart_container"
  #   Then I should be taken to the "cart" page 
  #    And I should see all of my items 
  #  Examples: 
  #  | items                                                                            |
  #  | Test.allTheThings() T-Shirt (Red)                                                | 
  #  | Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie             |

  # @sauce-003 @browser
  # Scenario Outline: The user can navigate to checkout step one
  #  Given I have a list of <items> to order
  #    And I am on the cart page
  #   When I click "checkout"
  #   Then I should be taken to the "checkout-step-one" page 
  # Examples: 
  #  | items                                                                            |
  #  | Sauce Labs Backpack, Sauce Labs Bike Light                                       |

  # @sauce-004 @browser
  # Scenario Outline: The user can enter their personal details
  #  Given I have a list of <items> to order
  #    And I am on the "checkout-step-one" page 
  #    And I enter my <first> name, <last> name, and <postal_code> 
  #   When I click "continue"
  #   Then I should be taken to the "checkout-step-two" page 
  # Examples: 
  #  | items                                        | first     | last    | postal_code |
  #  | Sauce Labs Onesie, Sauce Labs Fleece Jacket  | Joe       | Bloggs  | 101         |

  @sauce-005 @browser
  Scenario Outline: The user can review and finish their order 
   Given I have a list of <items> to order
     And I am on the "checkout-step-two" page 
    When I click "finish"
    Then I should be taken to the "checkout-complete" page 
     And I should see "Thank you for your order!"
  Examples: 
   | items                                                                            | 
   | Sauce Labs Backpack, Sauce Labs Bike Light                                       | 
   
   
   


