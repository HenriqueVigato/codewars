def filter_list(l)
  l.select { |i| i.is_a?(Integer) }
end

puts filter_list([1, 2, 3, 4, 'seis', 'sete', 8])
