function greatestProduct(input) {
  let n = input.length;
  let p = 10, temp;
  for (let i = 0; i < n-4; i++) {
    temp = Number(input[i])*Number(input[i+1])*Number(input[i+2])*Number(input[i+3])*Number(input[i+4]);
    if (temp > p) {
      p = temp;
    }
  }
  return temp;
}

function nthFibo(n) {
  let A = [0, 1];
  if (n < 2) {
    return A[n];
  }
  for (let i = 2; i <= n; i++) {
    A.push(A[i-1] + A[i-2]);
  }
  return A[n-1];
}

console.log(nthFibo(4));