README

input\districts.txt is a list of every districting arrangement (called a "state") when a 6x3 grid is broken into 6 equal-sized districts.

Each entry in districts.txt is [state, district, [first cell], [second cell], [third cell]].

There are 170 states, each with 6 districts. There are 170 * 6 = 1,020 entries in the file.

Each district is a group of 3 cells.

***

input\voterlocs.txt is a list of every arrangement of 6 voters on a 6x3 grid.

There are C(18,6) = 18,564 entries.

***

The methods I put in main.py try to respond to the question, which arrangements of voters are most/least gerrymanderable? I thought, for a given arrangement of voters, a histogram would be helpful. The histogram shows how much power a voter arrangement would have in different states. Let's say a voter arrangement has the histogram [170,0,0,0]. That means that in all 170 states, that voter arrangement controls zero districts. That arrangement of voters is not gerrymanderable. If the histogram is [10,30,50,80], then in 10 states this arrangement of voters controls 0 districts. In 30 states they control 1 district. In 50 states they control 2 districts. In 80 states they control 3 districts. (It's impossible for an arrangement of 6 voters on 18 squares to control more than 3 districts.) So this arrangement of voters is highly gerrymanderable: depending on how the state is designed, they can control 0, 1, 2, or 3 districts.

But, we still need to know exactly which states give which results. So StatesWithNDistrictsWon tells us exactly which states are part of each entry in the histogram.

One thing I have not figured out yet is how to use the contents of a file as input to a method. I have the files, and when I copy and paste them into the code, everything seems to work. But I don't know how to keep the input hidden in the file. That's why there's no testing here yet.

Let me know if this approach makes sense to you. Happy to talk it over any time. --Daniel