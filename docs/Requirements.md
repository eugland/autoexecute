# Requirements

Requirement A: Watch my Options and be able to close them within a margin of safety.
    - continously poll the stock market every minute from 9:30-4:00 EST
    - if the stock price is within (set_alert_range) of my target short position:
        - send alert that includes close cost, quantity, current option cost, and current stock price.   
        - change poll frequency to secondly
    - if the stock price is within (set_close_range) of my target long position, send alert
    
Requirement B: show me a table of option with their risk calculated
    - how to calculate risk?
        - TODO: find out more
        - 
    - profit: 
        - one side profit = (short position bid - long position ask) / spread distance
        - two side profit = add up and down side.
    - show a graph with distribution of profit to risk:

How to calculate risk?
- Black-Scholes option formula. In other words, Hood takes the Implied Volatility of the options you’re buying and plugs that into the equation, then spits out your chance of success