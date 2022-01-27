var searchRange = function(nums, target) {
    return [findFirst(nums,target),findLast(nums,target)];    
};

function findFirst(nums,target){
    let [start,end] = [0,nums.length-1];
    firstIdx = -1;
    
    while(start<=end){
        let mid = parseInt((start+end)/2,10);
        
        if(nums[mid] === target){
            firstIdx = mid;
            // 가장 작은 인덱스를 찾아야 하므로, 처음 발견한 곳을 마지막으로 가정하는 것
            end = mid-1;
        }else if(nums[mid] > target){
            end = mid-1;
        }else{
            start = mid+1;
        }
        
    }
    return firstIdx;
    
}

function findLast(nums,target){
    let [start,end] = [0,nums.length-1];
    lastIdx = -1;
    
    while(start<=end){
        let mid = parseInt((start+end)/2,10);
        
        if(nums[mid] === target){
            lastIdx = mid;
            // 가장 작은 인덱스를 찾아야 하므로, 처음 발견한 곳을 마지막으로 가정하는 것
            start = mid+1;
        }else if(nums[mid] > target){
            end = mid-1;
        }else{
            start = mid+1;
        }
        
    }
    return lastIdx;
}