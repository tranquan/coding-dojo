/**
 * Learning about Iterator and Generator
 */

function* makeIterator() {
  for (let i = 0; i < 3; i++) {
    yield i;
  }
}

function test1() {
  const iter = makeIterator();
  console.log(iter.next());
  console.log(iter.next());
  console.log(iter.next());
  console.log(iter.next());
}

function* fibonacciGenerator() {
  let current = 0;
  let next = 1;
  while (true) {
    yield current;
    [current, next] = [next, current + next];
  }
}

class FibonacciGenerator {
  current = 0;
  next = 1;

  reset() {
    this.current = 0;
    this.next = 1;
  }

  *[Symbol.iterator]() {
    while (true) {
      yield this.current;
      [this.current, this.next] = [this.next, this.current + this.next];
    }
  }
}

function test2() {
  const gen = new FibonacciGenerator();
  const iter = gen[Symbol.iterator]();
  console.log("---generate fibonacci");
  for (let i = 0; i < 3; i++) {
    console.log(iter.next());
  }
  console.log("---reset");
  gen.reset();
  for (let i = 0; i < 3; i++) {
    console.log(iter.next());
  }
}

// ---------------------------------------------
// Main
// test1();
test2();
