/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length === 1) return 0;
    let [profit,buyDay,sellDay,length] = [0,0,1,prices.length];
    while(sellDay<length){
        if(prices[buyDay] >= prices[sellDay]) {
            buyDay = sellDay;
            sellDay++;
            continue;
        }

        profit = Math.max(profit,prices[sellDay]-prices[buyDay]);
        sellDay++;
    }


    return profit
};