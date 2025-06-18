import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Car Salesman Decoder",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 10px 10px;
    }
    
    .tagline {
        text-align: center;
        font-size: 1.5rem;
        color: #2a5298;
        margin: 1rem 0;
        font-weight: 600;
    }
    
    .sub-tagline {
        text-align: center;
        font-size: 2rem;
        color: #1e3c72;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .section-header {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
    }
    
    .red-flag {
        background: #ffebee;
        border-left: 4px solid #f44336;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
    
    .defense-tip {
        background: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
    
    .psychology-insight {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
    
    .glossary-term {
        background: #f3e5f5;
        border-left: 4px solid #9c27b0;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
    
    .prep-item {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🚗 Navigation")
sections = [
    "🏠 Home",
    "🧠 Psychology",
    "🛡️ Defense Strategies", 
    "🚩 Red Flags",
    "📚 Glossary",
    "📋 Meeting Prep"
]

selected_section = st.sidebar.selectbox("Choose a section:", sections)

# Home Page
if selected_section == "🏠 Home":
    st.markdown("""
    <div class="main-header">
        <h1>🚗 Car Salesman Decoder</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tagline">
        Uncover hidden costs and conflicts of interest when you purchase a car.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sub-tagline">
        Don't Get Sold - Get Decoded
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 For Working Families
        - Garbage collectors
        - Plumbers  
        - Nurses
        - Electricians
        - Teachers
        - And everyone else who works hard for their money
        """)
    
    with col2:
        st.markdown("""
        ### 🚨 What We Expose
        - Financing markup schemes
        - Trade-in lowballing tactics
        - Monthly payment manipulation
        - Hidden fees and add-ons
        - Pressure selling techniques
        """)
    
    with col3:
        st.markdown("""
        ### 🛡️ What You'll Learn
        - How to spot manipulation
        - Negotiation strategies
        - Financing alternatives
        - When to walk away
        - Pre-purchase preparation
        """)

# Psychology Section
elif selected_section == "🧠 Psychology":
    st.markdown('<div class="section-header"><h2>🧠 Psychology Behind Car Sales</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding the psychological tactics used by car salespeople helps you maintain control and make rational decisions.
    """)
    
    st.markdown('<div class="psychology-insight">', unsafe_allow_html=True)
    st.markdown("""
    **🎭 The Friendly Facade**
    
    Salespeople are trained to become your "friend" within minutes. They'll ask about your family, job, and interests to:
    - Build false rapport and trust
    - Gather information about your financial situation
    - Make you feel guilty about negotiating with a "friend"
    - Create emotional attachment to override logical thinking
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="psychology-insight">', unsafe_allow_html=True)
    st.markdown("""
    **⏰ Time Pressure Tactics**
    
    "This deal expires today" or "Another customer is looking at this car" are classic manipulation techniques:
    - Creates artificial urgency to prevent comparison shopping
    - Triggers fear of missing out (FOMO)
    - Prevents you from sleeping on major financial decisions
    - Forces quick decisions that benefit the dealer, not you
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="psychology-insight">', unsafe_allow_html=True)
    st.markdown("""
    **💸 Monthly Payment Fixation**
    
    Focusing only on monthly payments is designed to hide the total cost:
    - Extends loan terms to reduce monthly payment while increasing total cost
    - Buries negative equity from trade-ins into new loans
    - Distracts from discussing actual vehicle price
    - Makes expensive cars seem "affordable"
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="psychology-insight">', unsafe_allow_html=True)
    st.markdown("""
    **🎯 Anchoring and Framing**
    
    Starting with high prices or payments to make subsequent offers seem reasonable:
    - Lists inflated sticker prices as "starting points"
    - Presents financing as "only $X more per month" 
    - Uses trade-in lowballing to justify higher sale prices
    - Frames expensive add-ons as "protection for your investment"
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Defense Strategies Section
elif selected_section == "🛡️ Defense Strategies":
    st.markdown('<div class="section-header"><h2>🛡️ Defense Strategies</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="defense-tip">', unsafe_allow_html=True)
    st.markdown("""
    **🏦 Secure Your Own Financing First**
    
    - Get pre-approved at your bank or credit union BEFORE shopping
    - Know your credit score and what rates you qualify for  
    - Use dealer financing only if they can beat your pre-approved rate
    - Never let them run your credit until you're ready to buy
    - Dealer financing markup can add thousands to your loan cost
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="defense-tip">', unsafe_allow_html=True)
    st.markdown("""
    **📊 Research Before You Go**
    
    - Use KBB, Edmunds, and AutoTrader to know fair market value
    - Research common problems for the specific make/model/year
    - Know the invoice price, not just MSRP
    - Check manufacturer incentives and rebates
    - Get trade-in estimates from multiple sources online
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="defense-tip">', unsafe_allow_html=True)
    st.markdown("""
    **🎯 Negotiate the Right Way**
    
    - Focus on TOTAL PRICE first, not monthly payments
    - Negotiate car price, trade-in value, and financing separately
    - Get all numbers in writing before signing anything
    - Be prepared to walk away - there are always other cars
    - Bring a calculator and verify all math yourself
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="defense-tip">', unsafe_allow_html=True)
    st.markdown("""
    **🚪 The Power of Walking Away**
    
    - Set a maximum budget and stick to it
    - Don't fall in love with any specific car
    - If pressured, say "I need to think about it" and leave
    - Real deals don't disappear overnight
    - Your best negotiating position is being willing to leave
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="defense-tip">', unsafe_allow_html=True)
    st.markdown("""
    **📝 Read Everything Carefully**
    
    - Review all paperwork line by line
    - Question every fee and add-on
    - Don't sign anything you don't understand
    - Take photos of all documents
    - Get copies of everything you sign
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Red Flags Section
elif selected_section == "🚩 Red Flags":
    st.markdown('<div class="section-header"><h2>🚩 Red Flags to Watch For</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="red-flag">', unsafe_allow_html=True)
    st.markdown("""
    **🚨 Financing Red Flags**
    
    - Won't tell you the interest rate upfront
    - Insists on running credit before showing you cars
    - Only discusses monthly payments, never total price
    - Claims their financing is "the best you'll qualify for"
    - Adds financing markup without disclosure
    - Tries to sell extended warranties in the finance office
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="red-flag">', unsafe_allow_html=True)
    st.markdown("""
    **💸 Trade-In Red Flags**
    
    - Won't appraise your trade-in until after you negotiate purchase price
    - Offers significantly less than KBB/Edmunds estimates without explanation
    - Tries to combine trade-in and purchase negotiations
    - Claims your car has problems they "just discovered"
    - Pressures you to decide on trade-in value immediately
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="red-flag">', unsafe_allow_html=True)
    st.markdown("""
    **⏰ Pressure Tactics Red Flags**
    
    - "This deal expires today"
    - "I have to check with my manager" (repeatedly)
    - "Another customer is interested in this car"
    - Won't let you take car for independent inspection
    - Rushes you through paperwork
    - Gets upset when you want to think about it
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="red-flag">', unsafe_allow_html=True)
    st.markdown("""
    **📄 Paperwork Red Flags**
    
    - Blank spaces in contracts
    - Add-ons you didn't agree to
    - Different numbers than what was discussed
    - Won't provide copies of documents
    - Excessive documentation fees (over $200)
    - Mandatory add-ons you can't remove
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="red-flag">', unsafe_allow_html=True)
    st.markdown("""
    **🎭 Behavioral Red Flags**
    
    - Immediately asks about monthly payment budget
    - Tries to separate you from family/friends during negotiations
    - Uses high-pressure emotional manipulation
    - Won't give you space to think or discuss with others
    - Makes you feel guilty for negotiating
    - Claims to be "losing money" on the deal
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Glossary Section
elif selected_section == "📚 Glossary":
    st.markdown('<div class="section-header"><h2>📚 Car Buying Glossary</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **APR (Annual Percentage Rate)**
    The total yearly cost of borrowing, including interest and fees. Always compare APRs, not just interest rates.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Financing Markup**
    When dealers add percentage points to the interest rate you qualify for and keep the difference as profit. Can cost thousands over the loan term.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Negative Equity (Being Upside Down)**
    When you owe more on your car loan than the car is worth. Often hidden by rolling it into a new loan.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Invoice Price**
    What the dealer actually paid for the car (before incentives). Usually lower than MSRP and a better starting point for negotiations.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **MSRP (Manufacturer's Suggested Retail Price)**
    The sticker price. It's a suggestion, not a requirement. Most cars sell for less than MSRP.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Doc Fee (Documentation Fee)**
    Fee charged for processing paperwork. Often inflated profit center. Reasonable range is $50-$200.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Dealer Holdback**
    Money manufacturers pay dealers after selling cars. Means dealers can profit even when selling at "invoice price."
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Lease Inception**
    Upfront costs when starting a lease, including first payment, security deposit, and fees. Often higher than advertised.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Gap Insurance**
    Covers difference between what you owe and car's value if totaled. Often overpriced at dealerships; check with your regular insurance first.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glossary-term">', unsafe_allow_html=True)
    st.markdown("""
    **Extended Warranty**
    Service contract covering repairs after manufacturer warranty expires. High markup item; research independent options.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Meeting Prep Section
elif selected_section == "📋 Meeting Prep":
    st.markdown('<div class="section-header"><h2>📋 Pre-Purchase Meeting Preparation</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📋 Checklist", "📊 Calculator", "📝 Notes"])
    
    with tab1:
        st.markdown("### Essential Preparation Checklist")
        
        st.markdown('<div class="prep-item">', unsafe_allow_html=True)
        st.markdown("""
        **🏦 Financial Preparation**
        - [ ] Check your credit score (annualcreditreport.com)
        - [ ] Get pre-approved for financing at your bank/credit union
        - [ ] Set maximum budget (total price, not monthly payment)
        - [ ] Research insurance costs for your target vehicles
        - [ ] Calculate total cost of ownership (gas, maintenance, insurance)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="prep-item">', unsafe_allow_html=True)
        st.markdown("""
        **🔍 Research Preparation**
        - [ ] Research target vehicles on KBB, Edmunds, AutoTrader
        - [ ] Know invoice price and current incentives/rebates
        - [ ] Research common problems for specific year/model
        - [ ] Get trade-in estimates from multiple online sources
        - [ ] Identify 3-5 similar vehicles at different dealers
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="prep-item">', unsafe_allow_html=True)
        st.markdown("""
        **📱 Bring With You**
        - [ ] Pre-approval letter from your bank
        - [ ] Calculator (phone calculator works)
        - [ ] Notepad and pen
        - [ ] Trade-in title and maintenance records
        - [ ] Driver's license and insurance card
        - [ ] This decoder guide for reference
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="prep-item">', unsafe_allow_html=True)
        st.markdown("""
        **🎯 Negotiation Strategy**
        - [ ] Decide on walk-away price before you go
        - [ ] Plan to negotiate total price first, not payments
        - [ ] Prepare responses to common pressure tactics
        - [ ] Identify your BATNA (Best Alternative to Negotiated Agreement)
        - [ ] Set aside emotional attachment to any specific car
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Payment Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            car_price = st.number_input("Car Price ($)", value=25000, step=1000)
            down_payment = st.number_input("Down Payment ($)", value=5000, step=500)
            trade_value = st.number_input("Trade-in Value ($)", value=0, step=500)
            interest_rate = st.number_input("Interest Rate (%)", value=6.0, step=0.1, format="%.1f")
            loan_term = st.selectbox("Loan Term (months)", [36, 48, 60, 72, 84])
        
        with col2:
            amount_financed = car_price - down_payment - trade_value
            monthly_rate = interest_rate / 100 / 12
            
            if monthly_rate > 0:
                monthly_payment = amount_financed * (monthly_rate * (1 + monthly_rate)**loan_term) / ((1 + monthly_rate)**loan_term - 1)
            else:
                monthly_payment = amount_financed / loan_term
            
            total_paid = monthly_payment * loan_term + down_payment + trade_value
            total_interest = total_paid - car_price
            
            st.metric("Amount Financed", f"${amount_financed:,.2f}")
            st.metric("Monthly Payment", f"${monthly_payment:.2f}")
            st.metric("Total Interest Paid", f"${total_interest:,.2f}")
            st.metric("Total Cost", f"${total_paid:,.2f}")
    
    with tab3:
        st.markdown("### Meeting Notes Template")
        
        st.markdown("""
        Use this template to track important information during your visit:
        
        **Dealership:** ________________________________
        **Date:** ______________________________________
        **Salesperson:** _______________________________
        
        **Vehicle Information:**
        - Make/Model/Year: ____________________________
        - VIN: _______________________________________
        - Mileage: ___________________________________
        - Condition Notes: ____________________________
        
        **Pricing:**
        - MSRP: $_____________________________________
        - Offered Price: $______________________________
        - Trade-in Offer: $_____________________________
        - Down Payment: $_____________________________
        
        **Financing:**
        - Interest Rate Offered: ________________________
        - Loan Term: ___________________________________
        - Monthly Payment: $____________________________
        - Total Amount Financed: $______________________
        
        **Red Flags Noted:**
        ____________________________________________
        ____________________________________________
        
        **Questions to Follow Up:**
        ____________________________________________
        ____________________________________________
        
        **Decision:** 
        [ ] Move forward
        [ ] Need to think about it
        [ ] Walk away
        
        **Next Steps:**
        ____________________________________________
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>💪 Built for working families who deserve honest car buying information</p>
    <p>🚗 Knowledge is your best defense against high-pressure sales tactics</p>
</div>
""", unsafe_allow_html=True)
