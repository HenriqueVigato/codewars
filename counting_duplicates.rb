def duplicate_count(text)
  duplicates = Hash.new(0)
  qt_duplicates = 0
  text.downcase.each_char.map do |char|
    duplicates[char] += 1
  end
  duplicates.each do |key, value|
    qt_duplicates += value > 1 ? 1 : 0
  end
  qt_duplicates
end

puts duplicate_count('llaranjan')
