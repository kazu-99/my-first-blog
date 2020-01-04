<b-modal :active.sync="startFlg"
         :canCancel="false">
  <button class="button is-info is-large"
          @click="startFlg=false; start()">Game Start</button>
</b-modal>

draw () {
  this.init()
  for (var b in this.block) {
    console.log('draw b: ' + this.block[b].x + ', ' + this.block[b].y + ', ' + this.gameTable[this.block[b].y][this.block[b].x])
    if (this.gameTable[this.block[b].y][this.block[b].x] === 0) {
      console.log('draw: ' + this.block[b].x + ', ' + this.block[b].y)
      this.gameTable[this.block[b].y].splice(this.block[b].x, 1, 1)
    }
  }
}

move (x, y) {
  this.init()
  for (var b in this.block) {
    this.block.splice(b, 1, {x: this.block[b].x + x, y: this.block[b].y + y})
  }
}

setBlock () {
  this.init()
  for (var b in this.block) {
    console.log('setBlock: ' + this.block[b].x + ', ' + this.block[b].y)
    this.gameTable[this.block[b].y].splice(this.block[b].x, 1, 2)
  } 
}

clearLine () {
  var line = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
  var clearLine = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for (var y = 0; y < this.gameTable.length; y++) {
    if (this.arrayCheck(this.gameTable[y], line)) {
      this.gameTable.splice(y, 1)
      this.gameTable.unshift(clearLine)
      this.score += 100
      this.level -= 5
    }
  }
}
