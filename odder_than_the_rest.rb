def oddOne(arr)
  odds = 0
  arr.each_with_index do |number, i|
    odds += i if number.odd?
  end
  odds > 0 ? odds : -1
end

puts oddOne([2, 6, 8, 4])
