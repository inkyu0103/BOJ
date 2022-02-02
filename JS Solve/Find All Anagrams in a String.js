/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */

/*
    1. p의 각각 문자마다, hash Map을 만들어 놓는다.
    2. s의 문자열에서 p.length 만큼 범위에 대해 추가한다.
    3. 모든 문자에 대해서 같은 값을 가지면, 만들 수 있으므로 answer에 추가

*/

var findAnagrams = function(s, p) {
    const pChars = p.split("");
    const answer = [];

    const[sLength,pLength] = [s.length,p.length];


    for(let i=0;i<=sLength-pLength;i++){
      const targetChars= s.substring(i,i+pLength).split("");
      if(DeepCompare(targetChars,pChars))
          answer.push(i);

    }

    return answer;
};

function DeepCompare(a,b){
    const newA = a.sort();
    const newB = b.sort();

    for(let i=0;i<newA.length;i++){
        if(newA[i] !== newB[i])
            return false;
    }

    return true

}




