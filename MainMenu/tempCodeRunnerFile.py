def sort_table_column(self, column, data, sort_algorithm):
        col_index = self.ui.table_schedule.horizontalHeader().visualIndex(column)
        column_data = [row[col_index] for row in data]
        sorted_column_data = sort_algorithm(data, col_index)

        # Assuming 'table_schedule' is your QTableWidget
        self.display_sorted_column(col_index, sorted_column_data)