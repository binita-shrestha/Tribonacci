function tribonacciSequence(startSequence, length) {
  if (length === 0) return [];
  if (length <= 3) return startSequence.slice(0,length);
  const seq = startSequence.slice(0,3);
  for (let i = 3; i < length; i++){
    const nextnum = seq[i-1]+seq[i-2]+seq[i-3];
    seq.push(nextnum);  
  }
  return seq;
}
console.log(tribonacciSequence([0,0,1],0));
console.log(tribonacciSequence([0,0,1],1));
console.log(tribonacciSequence([0,0,1],2));
console.log(tribonacciSequence([0,0,1],3));
console.log(tribonacciSequence([0,0,1],6));
console.log(tribonacciSequence([0,0,1],14));